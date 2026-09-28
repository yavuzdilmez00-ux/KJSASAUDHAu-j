import os
import json
import time
import random
import requests
from bs4 import BeautifulSoup
import trafilatura
from urllib.parse import urljoin, urlparse

ANA_KLASOR = "Hikayeler_Arsivi"

# Botun dalışa geçeceği başlangıç siteleri (İstersen buraya başka siteler de ekleyebilirsin)
BASLANGIC_SITELERI = [
    "https://dinihikayeler.com.tr/",
    "https://www.islamveihsan.com/dini-hikayeler",
    "https://www.islamidavet.com/kategoriler/hikayeler/"
]

def ayni_siteden_linkleri_bul(url, html_icerik):
    linkler = set()
    ana_domain = urlparse(url).netloc
    soup = BeautifulSoup(html_icerik, 'html.parser')
    
    for a_tag in soup.find_all("a", href=True):
        href = a_tag["href"]
        tam_url = urljoin(url, href)
        # Sadece aynı site içindeki linklere git (Reklamlara veya başka sitelere gitme)
        if urlparse(tam_url).netloc == ana_domain:
            linkler.add(tam_url)
    return linkler

def link_ziplayan_orumcek():
    if not os.path.exists(ANA_KLASOR):
        os.makedirs(ANA_KLASOR)

    dosya_yolu = os.path.join(ANA_KLASOR, "Otomatik_Toplananlar.json")
    mevcut_veriler = []
    
    if os.path.exists(dosya_yolu):
        try:
            with open(dosya_yolu, "r", encoding="utf-8") as f:
                mevcut_veriler = json.load(f)
        except json.JSONDecodeError:
            pass
            
    ziyaret_edilenler = {h.get('kaynak_url') for h in mevcut_veriler if 'kaynak_url' in h}
    ziyaret_edilecekler = set(BASLANGIC_SITELERI)
    
    # GitHub Action zaman aşımına uğramasın diye her çalışmada max 50 sayfa gezecek.
    # Her hafta otomatik çalıştığında kaldığı yerden devam edip yeni linkler bulacak.
    MAX_SAYFA_LIMITI = 50 
    ziyaret_edilen_sayi = 0
    yeni_eklenen_sayisi = 0

    print("🕸️ Örümcek Bot sitelere dalıyor...")

    while ziyaret_edilecekler and ziyaret_edilen_sayi < MAX_SAYFA_LIMITI:
        url = ziyaret_edilecekler.pop() # Listeden bir link al
        
        if url in ziyaret_edilenler:
            continue

        print(f"[{ziyaret_edilen_sayi+1}/{MAX_SAYFA_LIMITI}] İnceleniyor: {url}")
        ziyaret_edilenler.add(url)
        
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'}
            res = requests.get(url, headers=headers, timeout=10)
            
            if res.status_code != 200:
                continue
                
            # Sayfanın içindeki tüm linkleri bulup "ziyaret_edilecekler" torbasına at
            yeni_linkler = ayni_siteden_linkleri_bul(url, res.text)
            for link in yeni_linkler:
                if link not in ziyaret_edilenler:
                    ziyaret_edilecekler.add(link)
                    
            # Sayfanın ana metnini akıllı şekilde çek
            icerik = trafilatura.extract(res.text)
            soup_baslik = BeautifulSoup(res.text, 'html.parser')
            baslik = soup_baslik.title.string.strip() if soup_baslik.title else "Başlıksız"

            # Eğer metin 500 karakterden uzunsa (yani kategori/menü sayfası değil, gerçek bir hikayeyse)
            if icerik and len(icerik) > 500:
                mevcut_veriler.append({
                    "baslik": baslik,
                    "icerik": icerik,
                    "kaynak_url": url
                })
                yeni_eklenen_sayisi += 1
                print(f"✅ HİKAYE BULUNDU: {baslik}")
            
            ziyaret_edilen_sayi += 1
            # Siteler bot olduğumuzu anlamasın diye rastgele bekle
            time.sleep(random.uniform(1.0, 2.5))

        except Exception as e:
            print(f"Hata oluştu ({url}): {e}")

    # Toplanan verileri JSON olarak kaydet
    with open(dosya_yolu, 'w', encoding='utf-8') as f:
        json.dump(mevcut_veriler, f, ensure_ascii=False, indent=4)
        
    print(f"\n🎉 İşlem Tamam! Bu seansta {yeni_eklenen_sayisi} yeni hikaye bulundu.")
    print(f"📁 Toplam Arşiv Büyüklüğü: {len(mevcut_veriler)} hikaye.")

if __name__ == "__main__":
    link_ziplayan_orumcek()
