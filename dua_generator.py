import json
import random
import itertools
from datetime import datetime

# Yüz binlerce kombinasyon üretecek kelime havuzu
hitaplar = [
    "Allah'ım!", "Ya Rabbi!", "Ey Rabbimiz!", "Ya Rahman!", "Ya Rahim!", 
    "Ya Şafi!", "Ya Rezzak!", "Ya Fettah!", "Ey Alemlerin Rabbi!", "Ya Gafur!",
    "Ya Tevvab!", "Ya Halim!", "Ya Kerim!", "Ey Yüce Allah'ım!", "Rabbim!"
]

istekler = [
    "bize hidayet nasip eyle", "kalbimizi dinin üzere sabit kıl", "bize dünyada ve ahirette iyilik ver",
    "bize helal ve bol rızık ihsan eyle", "hastalıklarımıza şifa ver", "bizi salih kullarının arasına kat",
    "ilmimizi ve anlayışımızı artır", "bize sabır ve metanet ver", "ailemize huzur ve bereket ihsan eyle",
    "bizi cennetinle mükafatlandır", "bize merhametinle muamele et", "günahlarımızı bağışla ve bizi affet",
    "göğsümüzü genişlet ve işimizi kolaylaştır", "bize son nefeste imanla ölmeyi nasip et",
    "bize hakkı hak bilip ona uymayı nasip et", "bizi rızana uygun işler yapmaya muvaffak kıl",
    "bize şükreden bir kalp ve zikreden bir dil ver", "bize katından bir rahmet ver",
    "yolumuzu aydınlat ve bizi sırât-ı müstakîmden ayırma", "bize göz aydınlığı olacak eşler ve nesiller ver",
    "ömrümüzü bereketli kıl", "ibadetlerimizi kabul eyle", "dualarımızı geri çevirme", "bize sarsılmaz bir iman ver",
    "bizi rızana ulaştıracak amellere yönelt"
]

korunmalar = [
    "bizi cehennem azabından koru", "bizi kabir azabından muhafaza eyle", "bizi şeytanın vesveselerinden koru",
    "bizi görünmez kazalardan ve belalardan esirge", "bizi kötü ahlaktan ve hastalıklardan muhafaza et",
    "bizi zalimlerin şerrinden ve haksızlıklardan koru", "bizi nefsimizin şerrinden uzak tut",
    "bizi faydasız ilimden ve doymayan nefisten koru", "bizi fakirlikten ve borç altında ezilmekten esirge",
    "bizi fitne ve fesattan uzak tut", "bizi tembellikten ve acizlikten koru",
    "bizi dünyalık hırslardan ve kibrin şerrinden muhafaza eyle", "bizi sevdiklerimizle imtihan etme",
    "bizi şirkten ve riyadan koru", "bizi doğru yoldan saptıracak her türlü kötülükten esirge",
    "bizi kötü niyetli insanların şerrinden emin kıl", "bizi haktan ayrılmaktan muhafaza et",
    "bizi ansızın gelen belalardan koru", "bizi cimrilikten ve korkaklıktan esirge",
    "bizi hastalıklardan ve musibetlerden uzak tut", "bizi şeytanın adımlarını izlemekten koru",
    "bizi nankörlükten ve isyandan muhafaza eyle", "bizi gazabına uğramaktan koru",
    "bizi kötü akıbetten muhafaza et", "bizi şeytanlaşmış insanların tuzaklarından koru",
    "bizi dinimizde fitneye düşmekten koru", "bizi günahlara dalmaktan alıkoy",
    "bizi her türlü haramdan uzak tut", "bizi şeytanın maskaralığından koru",
    "bizi gaflet uykusundan uyandır ve koru", "bizi nefsimizin heveslerine uymaktan esirge",
    "bizi kaza ve kaderine isyan etmekten koru", "bizi ahiret azabından muhafaza et",
    "bizi darlık ve sıkıntılardan uzak tut", "bizi kötü arkadaşların şerrinden koru",
    "bizi her türlü zulümden ve haksızlıktan muhafaza eyle", "bizi utanç verici durumlara düşmekten koru",
    "bizi doğru yoldan sapanların arasına katılmaktan koru", "bizi zalim bir yöneticiye itaat etmekten koru",
    "bizi kendi nefsimize zulmetmekten koru"
]

kapanislar = [
    "Amin.", "Şüphesiz sen duaları hakkıyla işitensin.", 
    "Sen merhametlilerin en merhametlisisin.", "Dualarımızı dergâh-ı izzetinde kabul eyle.",
    "Şüphesiz senin her şeye gücün yeter.", "Bizi rahmetinden mahrum bırakma.",
    "Hamd, alemlerin Rabbi olan Allah'a mahsustur.", "Sen bizim Mevla'mızsın.",
    "Bizi affet, bizi bağışla, bize acı.", "Şüphesiz sen affedicisin, affetmeyi seversin."
]

def yuz_bin_dua_uret():
    print("Dualar oluşturuluyor, lütfen bekleyin...")
    
    # 1. Tüm olasılıkları hesapla (15 x 25 x 40 x 10 = 150.000 farklı dua)
    tum_kombinasyonlar = list(itertools.product(hitaplar, istekler, korunmalar, kapanislar))
    
    # 2. İçinden tam 100.000 tanesini rastgele seç
    secilen_kombinasyonlar = random.sample(tum_kombinasyonlar, 100000)
    
    # 3. Bunları JSON formatına uygun hale getir
    json_verisi = {
        "olusturulma_tarihi": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "toplam_dua_sayisi": len(secilen_kombinasyonlar),
        "dualar": []
    }
    
    for index, (hitap, istek, korunma, kapanis) in enumerate(secilen_kombinasyonlar, start=1):
        dua_metni = f"{hitap} {istek}, {korunma}. {kapanis}"
        json_verisi["dualar"].append({
            "id": index,
            "dua": dua_metni
        })
        
    return json_verisi

if __name__ == "__main__":
    # 100 Bin duayı üret
    dualar_sozlugu = yuz_bin_dua_uret()
    
    # JSON dosyasına yaz
    dosya_adi = "dualar.json"
    with open(dosya_adi, "w", encoding="utf-8") as json_dosyasi:
        json.dump(dualar_sozlugu, json_dosyasi, ensure_ascii=False, indent=4)
        
    print(f"Başarılı! Tam 100.000 farklı dua '{dosya_adi}' dosyasına JSON formatında kaydedildi.")
