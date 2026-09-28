import os
import json
import time
import random
from duckduckgo_search import DDGS
import trafilatura

ANA_KLASOR = "Hikayeler_Arsivi"

# Botun internette yapacağı aramalar ve bunları kaydedeceği klasör (kategori) isimleri
ARAMA_TERIMLERI = {
    "Asr-i_Saadet_ve_Sahabe": [
        "sahabe hayatından ibretlik hikayeler", 
        "peygamberimizin hayatından kıssalar"
    ],
    "Evliyalar_ve_Alimler": [
        "evliya hikayeleri yaşanmış", 
        "büyük islam alimlerinin ibretlik anıları"
    ],
    "Genel_Islami_Kissalar": [
        "yaşanmış dini hikayeler", 
        "ibretlik islami hikayeler uzun"
    ]
}

def akilli_orumcek_calistir():
    if not os.path.exists(ANA_KLASOR):
        os.makedirs(ANA_KLASOR)

    toplam_yeni_kayit = 0

    for kategori, aramalar in ARAMA_TERIMLERI.items():
        kategori_dosyasi = os.path.join(ANA_KLASOR, f"{kategori}.json")
        mevcut_veriler = []
        
        # Eski verileri oku ki aynı hikayeyi iki kere eklemeyelim
        if os.path.exists(kategori_dosyasi):
            try:
                with open(kategori_dosyasi, 'r', encoding='utf-8') as f:
                    mevcut_veriler = json.load(f)
            except json.JSONDecodeError:
                pass
                
        mevcut_linkler = {h.get('kaynak_url') for h in mevcut_veriler if 'kaynak_url' in h}
        mevcut_basliklar = {h.get('baslik') for h in mevcut_veriler if 'baslik' in h}

        print(f"\n[{kategori}] kategorisi için internette araştırma yapılıyor...")

        for kelime in aramalar:
            print(f"Arama Motorunda Aranıyor: '{kelime}'")
            try:
                # DuckDuckGo'dan her arama için 30 farklı web sitesi bul
                sonuclar = DDGS().text(kelime, region='tr-tr', max_results=30)
                
                for sonuc in sonuclar:
                    url = sonuc.get('href')
                    baslik = sonuc.get('title')

                    # Eğer bu siteyi daha önce kaydettiysek atla
                    if url in mevcut_linkler or baslik in mevcut_basliklar:
                        continue

                    print(f"Bağlanılıyor: {url}")
                    
                    # Siteye gir ve metni akıllı bir şekilde (HTML sormadan) çek
                    indirilen_sayfa = trafilatura.fetch_url(url)
                    if indirilen_sayfa:
                        icerik = trafilatura.extract(indirilen_sayfa)
                        
                        # Eğer geçerli bir metin bulduysa ve çok kısa değilse (menü vs. değilse) kaydet
                        if icerik and len(icerik) > 300:
                            mevcut_veriler.append({
                                "baslik": baslik,
                                "icerik": icerik,
                                "kaynak_url": url
                            })
                            mevcut_linkler.add(url)
                            toplam_yeni_kayit += 1
                            print("✅ Başarıyla çekildi ve listeye eklendi.")
                    
                    # Arama motorundan ban yememek için aralarda biraz bekle
                    time.sleep(random.uniform(1.5, 3.5))

            except Exception as e:
                print(f"Hata oluştu: {e}")
                time.sleep(5) # Hata olursa 5 saniye bekle, devam et

        # Bulunan tüm yeni verileri JSON olarak kaydet
        if mevcut_veriler:
            with open(kategori_dosyasi, 'w', encoding='utf-8') as f:
                json.dump(mevcut_veriler, f, ensure_ascii=False, indent=4)
            print(f"📁 {kategori}.json güncellendi. Toplam hikaye: {len(mevcut_veriler)}")

    print(f"\n🎉 İşlem Tamamlandı! Toplam {toplam_yeni_kayit} adet YENİ hikaye internetten bulunup kaydedildi.")

if __name__ == "__main__":
    akilli_orumcek_calistir()
