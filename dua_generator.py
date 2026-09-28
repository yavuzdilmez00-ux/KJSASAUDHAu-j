import json
import itertools
import os
from datetime import datetime

# 1. DOĞAL VE İÇTEN GİRİŞLER
hitaplar = [
    "Allah'ım!", "Rabbim!", "Ya Rabbi!", "Ey Yüce Rabbimiz!", 
    "Yüce Allah'ım!", "Ey merhameti sonsuz olan Rabbim!", 
    "Canım Allah'ım!", "Ey her şeyi yoktan var eden Rabbimiz!"
]

# 2. ŞÜKÜR VE YAKARIŞ CÜMLELERİ
ovguler = [
    "Bize verdiğin sayısız nimetler için sana sonsuz şükürler olsun,",
    "Senin rahmetin her şeyi kuşatmıştır,",
    "Biz aciz kullarınız, senin sonsuz kudretine sığındık,",
    "Yalnızca sana ibadet eder ve yalnızca senden yardım dileriz,",
    "Gönüllerimizdeki dertleri en iyi bilen sensin,",
    "Bizi yoktan var eden ve rızıklandıran sensin,",
    "Sen affedicisin, affetmeyi seversin,",
    "Bizim tek sığınağımız ve dayanağımız sensin,",
    "Sana açılan ellerimizi boş çevirme,",
    "Senin her şeye gücün yeter,",
    "Sonsuz merhametine güvenerek kapına geldik,",
    "Kusurlarımızı ve eksiklerimizi yalnız sen tamamlarsın,"
]

# 3. İSTEKLER VE LÜTUFLAR (KATEGORİLERE AYRILMIŞ HALDE)
istek_kategorileri = {
    "Iman_ve_Hidayet_Dualari": [
        "kalbimizi iman nuruyla doldur", 
        "hakkı hak bilip ona uymayı bize nasip et",
        "bizi rızana ulaştıracak güzel ahlak ile rızıklandır",
        "son nefesimizde kelime-i şehadet getirmeyi nasip eyle",
        "bizi sana layık bir kul, Peygamberimize layık bir ümmet eyle",
        "bizi doğru yoldan, sırât-ı müstakîmden ayırma"
    ],
    "Aile_ve_Huzur_Dualari": [
        "hanemize huzur, ömrümüze bereket ihsan eyle",
        "ailemizi ve sevdiklerimizi birbirine kenetle",
        "göğsümüze inşirah ver ve içimizi ferahlat",
        "bizi sevdiklerimizin acısıyla imtihan etme"
    ],
    "Rizik_ve_Is_Dualari": [
        "bize helal ve temiz rızıklar kapısı aç",
        "bize her işimizde kolaylıklar sağla",
        "işlerimizi hayırla sonuçlandır"
    ],
    "Sifa_ve_Afiyet_Dualari": [
        "bedenimize sıhhat, ruhumuza afiyet ver",
        "bize dert verip derman aratma"
    ],
    "Genel_Yenilenme_ve_Sabir_Dualari": [
        "ilmimizi, anlayışımızı ve sana olan sevgimizi artır",
        "bize dünyada da ahirette de iyilik ve güzellikler ver",
        "bize şükreden bir kalp ve zikreden bir dil bahşet",
        "karşılaştığımız zorluklarda bize sabır ve metanet ver",
        "dualarımızı katında makbul olan dualardan eyle"
    ]
}

# 4. KORUNMA VE SIĞINMA
korunmalar = [
    "ve bizi cehennem ateşinden koru", "ve nefsimizin bitmek bilmeyen heveslerinden bizi esirge", 
    "ve bizi şeytanın sinsi aldatmacalarından uzak tut", "ve görünmez kazalardan, beklenmedik belalardan bizi muhafaza eyle", 
    "ve bizi kötü ahlaktan, kinden ve hasetten arındır", "ve zalimlerin, kötü niyetli insanların şerrinden bizi koru", 
    "ve bizi darlıkta bırakıp namerde muhtaç etme", "ve bizi fayda vermeyen ilimden, ürpermeyen kalpten koru", 
    "ve bizi fakirlikten, altından kalkamayacağımız borçlardan esirge", "ve bizi ailemizle, canımızla, malımızla sınama", 
    "ve bizi tembellikten, acizlikten, bereketsizlikten koru", "ve bizi dünyalık hırsların esiri olmaktan muhafaza eyle", 
    "ve bizi şirkten, gösterişten ve kibrin her türlüsünden uzak tut", "ve ansızın gelecek olan musibetlerden bizi esirge", 
    "ve bizi haktan ayrılmaktan, adaletten sapmaktan muhafaza et", "ve bizi hastalıkların yıpratıcı etkilerinden koru",
    "ve şeytanlaşmış insanların tuzaklarına düşmekten bizi koru", "ve ahirette yüzümüzü kara çıkartacak günahlardan bizi alıkoy",
    "ve bizi kaza ve kaderine isyan edenlerden eyleme", "ve bizi doğru yoldan sapanların arasına katılmaktan koru"
]

# 5. KAPANIŞLAR
kapanislar = [
    "Amin.", "Şüphesiz sen duaları hakkıyla işitensin. Amin.", 
    "Sen merhametlilerin en merhametlisisin.", "Dualarımızı dergâh-ı izzetinde kabul buyur.",
    "Bizi rahmetinden mahrum bırakma Rabbim.", "Hamd, alemlerin Rabbi olan Allah'a mahsustur.", 
    "Sen bizim yegâne Mevla'mızsın.", "Bizi affet, bizi bağışla, bize acı. Amin.", 
    "Şüphesiz senin her şeye gücün yeter."
]

def kategorileri_ayri_dosyalara_yaz():
    # 1. Ana klasörü oluştur (varsa hata vermez)
    klasor_adi = "dualar_klasoru"
    os.makedirs(klasor_adi, exist_ok=True)

    print("Dualar üretiliyor ve dosyalara ayrılıyor...")
    
    # 2. Her kategori için döngü başlat
    for kategori_adi, kategori_istekleri in istek_kategorileri.items():
        # Sadece o kategoriye ait kombinasyonları hesapla
        kombinasyonlar = list(itertools.product(hitaplar, ovguler, kategori_istekleri, korunmalar, kapanislar))
        
        kategori_verisi = {
            "olusturulma_tarihi": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "kategori_adi": kategori_adi,
            "toplam_dua_sayisi": len(kombinasyonlar),
            "dualar": []
        }
        
        for index, (hitap, ovgu, istek, korunma, kapanis) in enumerate(kombinasyonlar, start=1):
            dua_metni = f"{hitap} {ovgu} {istek}, {korunma}. {kapanis}"
            kategori_verisi["dualar"].append({
                "id": index,
                "dua": dua_metni
            })
        
        # 3. O kategoriye ait JSON dosyasını oluştur ve klasörün içine kaydet
        dosya_yolu = os.path.join(klasor_adi, f"{kategori_adi}.json")
        with open(dosya_yolu, "w", encoding="utf-8") as json_dosyasi:
            json.dump(kategori_verisi, json_dosyasi, ensure_ascii=False, indent=4)
            
        print(f" -> {dosya_yolu} başarıyla oluşturuldu ({len(kombinasyonlar)} dua).")

if __name__ == "__main__":
    kategorileri_ayri_dosyalara_yaz()
    print("Tüm işlemler tamamlandı!")
