import requests
from bs4 import BeautifulSoup
import json
import os

# Kazımak (scrape) istediğin sitelerin listesi (Gelecekte burayı çoğaltabilirsin)
KAYNAK_SITELER = [
    "https://ornek-islami-site.com/hikayeler"
]

ANA_KLASOR = "Hikayeler_Arsivi"

def genis_arsiv_getir():
    # İnternetten çekilemediği durumda eklenecek, dünyadan ve Türkiye'den çeşitli tarihi/İslami hikayeler
    return [
        {
            "baslik": "Hz. Ömer'in Adaleti ve Gece Bekçiliği",
            "icerik": "Hz. Ömer (r.a.) halifeliği döneminde bir gece Medine sokaklarında gezerken, ağlayan çocuk sesleri duydu. Yaklaştığında, bir annenin tencerede sadece su ve taş kaynatarak çocuklarını oyaladığını gördü. Durumu öğrenen halife, hemen beytülmalden erzak yüklenip kendi sırtında o eve taşıdı.",
            "kategori": "Asr-i_Saadet",
            "kaynak_bolge": "Arap Yarımadası"
        },
        {
            "baslik": "Fatih Sultan Mehmet ve Kadı Hızır Bey",
            "icerik": "Fatih Sultan Mehmet, bir cami inşaatında sütunları izinsiz kestiren Rum mimarın ellerini kestirir. Mimar, Padişahı Kadı Hızır Bey'e şikayet eder. Mahkemede Kadı, Padişahı haksız bulur ve kısas (padişahın da elinin kesilmesi) cezası verir. Mimar bu mutlak adalet karşısında şaşırıp davasından vazgeçer ve Müslüman olur.",
            "kategori": "Osmanli_Tarihi",
            "kaynak_bolge": "Türkiye / İstanbul"
        },
        {
            "baslik": "Mevlana ve İncir Satan Çocuk",
            "icerik": "Hz. Mevlana bir gün yolda ağlayan bir çocuk görür. Çocuğun elindeki incir sepeti devrilmiş ve incirler çamura bulanmıştır. Mevlana çocuğun yanına oturur, çamurlu incirleri kendi cübbesine silerek temizler, satın alır ve çocuğun yüzünü güldürür. Çevresindekilere 'Şu çocuğun kırık kalbini onarmak, binlerce rekat nafile namazdan evladır' der.",
            "kategori": "Tasavvuf_ve_Evliyalar",
            "kaynak_bolge": "Türkiye / Anadolu"
        },
        {
            "baslik": "Endülüs'te Bir Alim: İbn Rüşd'ün Gözyaşları",
            "icerik": "Büyük İslam alimi İbn Rüşd'ün kitapları, siyasi sebeplerle Endülüs meydanında yakılırken öğrencisi ağlamaya başlar. İbn Rüşd öğrencisine döner ve şöyle der: 'Eğer kitaplar için ağlıyorsan bil ki fikirlerin kanatları vardır, hak ettikleri yere uçarlar. Ama eğer İslam'ın bu duruma düşmesine ağlıyorsan, okyanusların suyu bile senin gözyaşlarına yetmez.'",
            "kategori": "Dunya_Tarihi_ve_Alimler",
            "kaynak_bolge": "Endülüs / İspanya"
        },
        {
            "baslik": "Yunus Emre'nin Buğdayı",
            "icerik": "Yunus Emre, kıtlık zamanında Hacı Bektaş Veli'nin dergahına buğday istemeye gider. Hacı Bektaş ona 'Buğday mı istersin, nefes mi?' diye sorar. Yunus, ailesinin açlığını düşünerek buğdayı seçer. Ancak yola çıktıktan sonra pişman olur ve 'Bana nefes gerek' diyerek geri döner, hakikat yolculuğu böyle başlar.",
            "kategori": "Tasavvuf_ve_Evliyalar",
            "kaynak_bolge": "Türkiye / Anadolu"
        }
    ]

def hikayeleri_cek():
    yeni_hikayeler = []
    # Gerçek bir siteden veri çekerken BeautifulSoup kodları buraya eklenebilir.
    # Şimdilik geniş arşivimizi varsayılan olarak döndürüyoruz.
    yeni_hikayeler.extend(genis_arsiv_getir())
    return yeni_hikayeler

def kategorilere_ayir_ve_kaydet(veriler):
    # Ana klasörü oluştur (yoksa)
    if not os.path.exists(ANA_KLASOR):
        os.makedirs(ANA_KLASOR)

    # Verileri kategorilerine göre grupla
    kategori_sozlugu = {}
    for hikaye in veriler:
        kategori_adi = hikaye.get("kategori", "Diger_Hikayeler")
        if kategori_adi not in kategori_sozlugu:
            kategori_sozlugu[kategori_adi] = []
        kategori_sozlugu[kategori_adi].append(hikaye)

    # Her kategori için ayrı bir JSON dosyası oluştur/güncelle
    for kategori, hikayeler in kategori_sozlugu.items():
        dosya_yolu = os.path.join(ANA_KLASOR, f"{kategori}.json")
        mevcut_veriler = []

        # Eğer o kategoriye ait dosya zaten varsa oku
        if os.path.exists(dosya_yolu):
            try:
                with open(dosya_yolu, 'r', encoding='utf-8') as f:
                    mevcut_veriler = json.load(f)
            except json.JSONDecodeError:
                pass

        # Tekrar eden hikayeleri engelle (başlığa göre kontrol et)
        mevcut_basliklar = {h.get('baslik') for h in mevcut_veriler}
        eklenen_sayisi = 0

        for hikaye in hikayeler:
            if hikaye['baslik'] not in mevcut_basliklar:
                mevcut_veriler.append(hikaye)
                eklenen_sayisi += 1

        # Dosyayı güncellenmiş haliyle tekrar kaydet
        if eklenen_sayisi > 0 or not os.path.exists(dosya_yolu):
            with open(dosya_yolu, 'w', encoding='utf-8') as f:
                json.dump(mevcut_veriler, f, ensure_ascii=False, indent=4)
            print(f"[{kategori}] kategorisine {eklenen_sayisi} yeni hikaye eklendi.")
        else:
            print(f"[{kategori}] kategorisinde yeni hikaye bulunamadı.")

if __name__ == "__main__":
    print("Hikayeler toplanıyor ve türlerine göre ayrılıyor...")
    toplanan_veriler = hikayeleri_cek()
    kategorilere_ayir_ve_kaydet(toplanan_veriler)
    print("İşlem başarıyla tamamlandı!")
