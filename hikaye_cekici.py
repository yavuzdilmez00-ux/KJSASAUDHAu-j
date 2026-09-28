import requests
from bs4 import BeautifulSoup
import json
import os

# Veri çekmek istediğin sitenin URL'sini buraya eklemelisin.
# Gerçek bir siteden veri çekerken HTML etiketlerini siteye göre düzenlemelisin.
HEDEF_URL = "https://ornek-islami-site.com/yasanmis-hikayeler"

def hikayeleri_cek():
    yeni_hikayeler = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    print("İnternetteki kaynaklar taranıyor...")
    
    try:
        response = requests.get(HEDEF_URL, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Sitenin yapısına göre bu kısımlar değişmelidir ('article', 'div' vs.)
            makaleler = soup.find_all('article', class_='hikaye')
            
            for makale in makaleler:
                baslik = makale.find('h2').text.strip() if makale.find('h2') else "Başlıksız"
                icerik = makale.find('div', class_='icerik').text.strip() if makale.find('div', class_='icerik') else ""
                
                if icerik: # İçi boş değilse ekle
                    yeni_hikayeler.append({
                        "baslik": baslik,
                        "icerik": icerik,
                        "kategori": "Yaşanmış İslami Hikayeler",
                        "dil": "tr"
                    })
    except Exception as e:
        print(f"Bağlantı hatası: {e}")

    # Eğer site bağlantısı ayarlanamadıysa sistemin boş kalmaması için örnek veri tabanı:
    if not yeni_hikayeler:
        print("Hedef siteye ulaşılamadı. Temel arşiv verileri kontrol ediliyor...")
        yeni_hikayeler = [
            {
                "baslik": "Hz. Ömer'in Adaleti ve Gece Bekçiliği",
                "icerik": "Hz. Ömer (r.a.) halifeliği döneminde bir gece Medine sokaklarında gezerken, ağlayan çocuk sesleri duydu. Yaklaştığında, bir annenin tencerede sadece su ve taş kaynatarak çocuklarını oyaladığını gördü. Durumu öğrenen halife, hemen beytülmalden erzak yüklenip kendi sırtında o eve taşıdı ve yemek pişene kadar oradan ayrılmadı.",
                "kategori": "Yaşanmış İslami Hikayeler",
                "dil": "tr"
            },
            {
                "baslik": "Cömertliğin Zirvesi",
                "icerik": "Bir gün Peygamber Efendimiz'e (s.a.v) bir misafir geldi. Evde yiyecek bir şey yoktu. Sahabelerden biri misafiri evine götürdü. Ancak onun da evinde sadece çocuklarına yetecek kadar yemek vardı. Hanımıyla anlaşıp çocukları uyuttular, yemeği misafire sundular ve misafir utanmasın diye kandili söndürüp kendileri de yiyormuş gibi yaptılar.",
                "kategori": "Yaşanmış İslami Hikayeler",
                "dil": "tr"
            }
        ]
        
    return yeni_hikayeler

def json_olarak_birlestir_ve_kaydet(veriler, dosya_adi="hikayeler.json"):
    mevcut_veriler = []
    
    # Mevcut JSON dosyasını oku (eski hikayeleri kaybetmemek için)
    if os.path.exists(dosya_adi):
        try:
            with open(dosya_adi, 'r', encoding='utf-8') as f:
                mevcut_veriler = json.load(f)
        except json.JSONDecodeError:
            print("Mevcut JSON dosyası okunamadı, sıfırdan başlanıyor.")

    # Aynı başlıkta hikaye varsa tekrar ekleme
    mevcut_basliklar = {hikaye.get('baslik') for hikaye in mevcut_veriler}
    
    eklenen_sayisi = 0
    for veri in veriler:
        if veri['baslik'] not in mevcut_basliklar:
            mevcut_veriler.append(veri)
            eklenen_sayisi += 1

    # Tüm verileri Türkçe karakterleri bozmadan JSON formatında yaz
    with open(dosya_adi, 'w', encoding='utf-8') as f:
        json.dump(mevcut_veriler, f, ensure_ascii=False, indent=4)
        
    print(f"İşlem tamam! {eklenen_sayisi} adet yeni hikaye '{dosya_adi}' dosyasına başarıyla yazıldı.")

if __name__ == "__main__":
    toplanan_veriler = hikayeleri_cek()
    json_olarak_birlestir_ve_kaydet(toplanan_veriler)
