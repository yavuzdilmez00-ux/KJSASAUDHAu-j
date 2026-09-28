import json
import itertools
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

def kategorili_dualari_uret():
    json_verisi = {
        "olusturulma_tarihi": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "toplam_dua_sayisi": 0,
        "kategoriler": {}
    }
    
    genel_id_sayaci = 1
    
    # Her kategori için ayrı ayrı kombinasyon oluşturuyoruz
    for kategori_adi, kategori_istekleri in istek_kategorileri.items():
        json_verisi["kategoriler"][kategori_adi] = []
        
        # O kategoriye ait isteklerle kombinasyon yapıyoruz
        kombinasyonlar = list(itertools.product(hitaplar, ovguler, kategori_istekleri, korunmalar, kapanislar))
        
        for (hitap, ovgu, istek, korunma, kapanis) in kombinasyonlar:
            dua_metni = f"{hitap} {ovgu} {istek}, {korunma}. {kapanis}"
            
            json_verisi["kategoriler"][kategori_adi].append({
                "id": genel_id_sayaci,
                "dua": dua_metni
            })
            genel_id_sayaci += 1

    json_verisi["toplam_dua_sayisi"] = genel_id_sayaci - 1
    return json_verisi

if __name__ == "__main__":
    dualar_sozlugu = kategorili_dualari_uret()
    
    # Eskisini tamamen silip yeni JSON dosyasına yaz
    dosya_adi = "dualar.json"
    with open(dosya_adi, "w", encoding="utf-8") as json_dosyasi:
        json.dump(dualar_sozlugu, json_dosyasi, ensure_ascii=False, indent=4)
        
    print(f"Başarılı! Toplam {dualar_sozlugu['toplam_dua_sayisi']} adet dua KATEGORİLERİNE AYRILARAK {dosya_adi} dosyasına kaydedildi.")
