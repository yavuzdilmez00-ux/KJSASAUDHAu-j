import json
import random
import itertools
from datetime import datetime

# 1. DOĞAL VE İÇTEN GİRİŞLER (Esma-ül Hüsna kalıpları çıkarıldı)
hitaplar = [
    "Allah'ım!", "Rabbim!", "Ya Rabbi!", "Ey Yüce Rabbimiz!", 
    "Yüce Allah'ım!", "Ey merhameti sonsuz olan Rabbim!", 
    "Canım Allah'ım!", "Ey her şeyi yoktan var eden Rabbimiz!"
]

# 2. DUALARI ZENGİNLEŞTİREN ŞÜKÜR VE YAKARIŞ CÜMLELERİ (Hepsi birbirine benzemesin diye)
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

# 3. İSTEKLER VE LÜTUFLAR
istekler = [
    "kalbimizi iman nuruyla doldur", "hakkı hak bilip ona uymayı bize nasip et", 
    "hanemize huzur, ömrümüze bereket ihsan eyle", "bize helal ve temiz rızıklar kapısı aç", 
    "bedenimize sıhhat, ruhumuza afiyet ver", "bizi rızana ulaştıracak güzel ahlak ile rızıklandır",
    "ilnimizi, anlayışımızı ve sana olan sevgimizi artır", "bize her işimizde kolaylıklar sağla", 
    "ailemizi ve sevdiklerimizi birbirine kenetle", "bize dünyada da ahirette de iyilik ve güzellikler ver", 
    "son nefesimizde kelime-i şehadet getirmeyi nasip eyle", "bizi sana layık bir kul, Peygamberimize layık bir ümmet eyle",
    "göğsümüze inşirah ver ve içimizi ferahlat", "bize şükreden bir kalp ve zikreden bir dil bahşet",
    "karşılaştığımız zorluklarda bize sabır ve metanet ver", "bizi doğru yoldan, sırât-ı müstakîmden ayırma",
    "işlerimizi hayırla sonuçlandır", "dualarımızı katında makbul olan dualardan eyle",
    "bize dert verip derman aratma", "bizi sevdiklerimizin acısıyla imtihan etme"
]

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

def yuz_bin_dogal_dua_uret():
    print("Doğal ve içten dualar oluşturuluyor, lütfen bekleyin...")
    
    # 1. Tüm olasılıkları hesapla (8 x 12 x 20 x 20 x 9 = 345.600 farklı eşsiz kombinasyon)
    tum_kombinasyonlar = list(itertools.product(hitaplar, ovguler, istekler, korunmalar, kapanislar))
    
    # 2. İçinden tam 100.000 tanesini rastgele seç
    secilen_kombinasyonlar = random.sample(tum_kombinasyonlar, 100000)
    
    # 3. Bunları JSON formatına uygun hale getir
    json_verisi = {
        "olusturulma_tarihi": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "toplam_dua_sayisi": len(secilen_kombinasyonlar),
        "dualar": []
    }
    
    for index, (hitap, ovgu, istek, korunma, kapanis) in enumerate(secilen_kombinasyonlar, start=1):
        # Cümleleri doğal bir şekilde birleştiriyoruz
        dua_metni = f"{hitap} {ovgu} {istek}, {korunma}. {kapanis}"
        
        json_verisi["dualar"].append({
            "id": index,
            "dua": dua_metni
        })
        
    return json_verisi

if __name__ == "__main__":
    # 100 Bin duayı üret
    dualar_sozlugu = yuz_bin_dogal_dua_uret()
    
    # JSON dosyasına yaz
    dosya_adi = "dualar.json"
    with open(dosya_adi, "w", encoding="utf-8") as json_dosyasi:
        json.dump(dualar_sozlugu, json_dosyasi, ensure_ascii=False, indent=4)
        
    print(f"Başarılı! Tamamen birbirinden farklı, doğal 100.000 dua '{dosya_adi}' dosyasına JSON formatında kaydedildi.")
