import requests
from bs4 import BeautifulSoup
import json
import os
import time
import random

ANA_KLASOR = "Hikayeler_Arsivi"
# İnternette binlerce hikayesi olan gerçek bir sitenin yapısını buraya girmelisin.
# {sayfa} kısmı döngü içinde 1, 2, 3... 1000 olarak değişecek.
HEDEF_SITELER = [
    {"url": "https://ornek-islami-site.com/yasanmis-hikayeler?sayfa={sayfa}", "max_sayfa": 500},
    {"url": "https://baska-tarih-sitesi.com/arsiv/sayfa/{sayfa}", "max_sayfa": 300}
]

def on_binlerce_hikaye_cek():
    tum_hikayeler = []
    
    # Sitelerin seni bot olarak algılayıp engellememesi için tarayıcı kimliği
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }

    for site in HEDEF_SITELER:
        print(f"\n--- {site['url'].split('/')[2]} sitesi taranmaya başlanıyor ---")
        
        # 1. sayfadan başlayıp sitenin maksimum sayfasına kadar tara
        for sayfa_no in range(1, site["max_sayfa"] + 1):
            guncel_url = site["url"].format(sayfa=sayfa_no)
            print(f"Taraniyor: {guncel_url}")
            
            try:
                response = requests.get(guncel_url, headers=headers, timeout=10)
                
                if response.status_code != 200:
                    print(f"Hata! Sayfa okunamadı. Kod: {response.status_code}")
                    break # Sayfalar bitmiş veya engellenmiş olabilir, diğer siteye geç

                soup = BeautifulSoup(response.text, 'html.parser')
                
                # DİKKAT: Buradaki 'div' ve 'class' isimlerini hedef sitenin kodlarına göre GÜNCELLEMELİSİN.
                makaleler = soup.find_all('div', class_='hikaye-karti') 
                
                if not makaleler:
                    print("Bu sayfada hikaye bulunamadı, muhtemelen son sayfaya gelindi.")
                    break

                for makale in makaleler:
                    try:
                        baslik = makale.find('h2').text.strip()
                        icerik = makale.find('div', class_='hikaye-metni').text.strip()
                        # Siteden kategori çekilemiyorsa varsayılan bir kategori ata
                        kategori = makale.find('span', class_='kategori-etiketi')
                        kategori_adi = kategori.text.strip().replace(" ", "_") if kategori else "Genel_Tarih"

                        tum_hikayeler.append({
                            "baslik": baslik,
                            "icerik": icerik,
                            "kategori": kategori_adi
                        })
                    except AttributeError:
                        continue # Eğer başlık veya içerik eksikse bu makaleyi atla

            except Exception as e:
                print(f"Bağlantı hatası oluştu: {e}")
            
            # BAN YEMEMEK İÇİN KRİTİK KISIM: 
            # Her sayfa geçişinde rastgele 1 ila 3 saniye bekle ki siteye saldırı yapıldığı sanılmasın.
            time.sleep(random.uniform(1.0, 3.0))

    return tum_hikayeler

def kategorilere_ayir_ve_kaydet(veriler):
    if not os.path.exists(ANA_KLASOR):
        os.makedirs(ANA_KLASOR)

    kategori_sozlugu = {}
    for hikaye in veriler:
        kat = hikaye.get("kategori", "Diger")
        if kat not in kategori_sozlugu:
            kategori_sozlugu[kat] = []
        kategori_sozlugu[kat].append(hikaye)

    toplam_eklenen = 0

    for kategori, hikayeler in kategori_sozlugu.items():
        dosya_yolu = os.path.join(ANA_KLASOR, f"{kategori}.json")
        mevcut_veriler = []

        if os.path.exists(dosya_yolu):
            try:
                with open(dosya_yolu, 'r', encoding='utf-8') as f:
                    mevcut_veriler = json.load(f)
            except json.JSONDecodeError:
                pass

        mevcut_basliklar = {h.get('baslik') for h in mevcut_veriler}
        
        eklenen_sayisi = 0
        for hikaye in hikayeler:
            if hikaye['baslik'] not in mevcut_basliklar:
                mevcut_veriler.append(hikaye)
                eklenen_sayisi += 1
                toplam_eklenen += 1

        if eklenen_sayisi > 0:
            with open(dosya_yolu, 'w', encoding='utf-8') as f:
                json.dump(mevcut_veriler, f, ensure_ascii=False, indent=4)
            print(f"[{kategori}]: +{eklenen_sayisi} yeni hikaye eklendi. (Toplam bu kategoride: {len(mevcut_veriler)})")

    print(f"\nİşlem bitti! Toplam {toplam_eklenen} YENİ hikaye çekildi ve klasörlere kaydedildi.")

if __name__ == "__main__":
    yeni_veriler = on_binlerce_hikaye_cek()
    if yeni_veriler:
        kategorilere_ayir_ve_kaydet(yeni_veriler)
    else:
        print("Hiç veri çekilemedi. Lütfen sitenin URL'sini ve HTML (div/class) etiketlerini kontrol et.")
