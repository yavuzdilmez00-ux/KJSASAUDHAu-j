import json
import random

# 1. Dua Bileşenleri (Bu listelerdeki kelimeler birleştirilerek dualar oluşturulacak)
hitaplar = [
    "Allah'ım!", "Ya Rabbi!", "Ey Rabbimiz!", "Ya Rahman!", "Ya Rahim!", 
    "Ya Şafi!", "Ya Rezzak!", "Ya Fettah!", "Ey Alemlerin Rabbi!", "Ya Gafur!",
    "Ya Tevvab!", "Ya Halim!", "Ya Kerim!", "Ey Yüce Allah'ım!", "Rabbim!"
]

istekler = [
    "bize hidayet nasip eyle", "kalbimizi dinin üzere sabit kıl", "bize dünyada ve ahirette iyilik ver",
    "bize helal ve bol rızık ihsan eyle", "hastalıklarımıza şifa ver", "bizi salih kullarının arasına kat",
    "ilnimizi ve anlayışımızı artır", "bize sabır ve metanet ver", "ailememize huzur ve bereket ihsan eyle",
    "bizi cennetinle mükafatlandır", "bize merhametinle muamele et", "günahlarımızı bağışla ve bizi affet",
    "göğsümüzü genişlet ve işimizi kolaylaştır", "bize son nefeste imanla ölmeyi nasip et",
    "bize hakkı hak bilip ona uymayı nasip et", "bizi rızana uygun işler yapmaya muvaffak kıl",
    "bize şükreden bir kalp ve zikreden bir dil ver", "bize katından bir rahmet ver",
    "yolumuzu aydınlat ve bizi sırât-ı müstakîmden ayırma", "bize göz aydınlığı olacak eşler ve nesiller ver"
]

korunmalar = [
    "bizi cehennem azabından koru", "bizi kabir azabından muhafaza eyle", "bizi şeytanın vesveselerinden koru",
    "bizi nefsimizin şerrinden uzak tut", "bizi görünmez kazalardan ve belalardan esirge",
    "bizi faydasız ilimden ve doymayan nefisten koru", "bizi kötü ahlaktan ve hastalıklardan muhafaza et",
    "bizi zalimlerin şerrinden ve haksızlıklardan koru", "bizi fakirlikten ve borç altında ezilmekten esirge",
    "bizi fitne ve fesattan uzak tut", "bizi tembellikten ve acizlikten koru",
    "bizi dünyalık hırslardan ve kibrin şerrinden muhafaza eyle",
    "bizi sevdiklerimizle imtihan etme", "bizi şirkten ve riyadan koru",
    "bizi doğru yoldan saptıracak her türlü kötülükten esirge"
]

kapanislar = [
    "Amin.", "Şüphesiz sen duaları hakkıyla işitensin.", 
    "Sen merhametlilerin en merhametlisisin.", "Şüphesiz senin her şeye gücün yeter.",
    "Dualarımızı dergâh-ı izzetinde kabul eyle.", "Bizi rahmetinden mahrum bırakma.",
    "Hamd, alemlerin Rabbi olan Allah'a mahsustur."
]

def on_yuzbin_dua_uret():
    uretilen_dualar = set() # Aynı duaların tekrar etmesini önlemek için set kullanıyoruz
    hedef_sayi = 100000
    
    print("Dualar oluşturuluyor, lütfen bekleyin...")
    
    while len(uretilen_dualar) < hedef_sayi:
        # Her kategoriden rastgele bir parça seç
        hitap = random.choice(hitaplar)
        istek = random.choice(istekler)
        korunma = random.choice(korunmalar)
        kapanis = random.choice(kapanislar)
        
        # Parçaları anlamlı bir cümle halinde birleştir
        dua_metni = f"{hitap} {istek}, {korunma}. {kapanis}"
        uretilen_dualar.add(dua_metni)

    # JSON formatına uygun hale getirmek için liste içine sözlükler (dict) oluşturuyoruz
    json_verisi = []
    for index, dua in enumerate(uretilen_dualar, start=1):
        json_verisi.append({
            "id": index,
            "dua": dua
        })
        
    return json_verisi

if __name__ == "__main__":
    dualar_listesi = on_yuzbin_dua_uret()
    
    # JSON dosyasına yazma işlemi
    dosya_adi = "100bin_dua.json"
    with open(dosya_adi, "w", encoding="utf-8") as json_dosyasi:
        json.dump(dualar_listesi, json_dosyasi, ensure_ascii=False, indent=4)
        
    print(f"Başarılı! 100.000 farklı dua '{dosya_adi}' dosyasına JSON formatında kaydedildi.")
