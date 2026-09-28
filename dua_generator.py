import json
import random
from datetime import datetime

# Yüz binlerce kombinasyon üretecek kelime havuzu
hitaplar = [
    "Allah'ım!", "Ya Rabbi!", "Ey Rabbimiz!", "Ya Rahman!", "Ya Şafi!", 
    "Ya Rezzak!", "Ya Fettah!", "Ey Alemlerin Rabbi!"
]
istekler = [
    "bize hidayet nasip eyle", "kalbimizi dinin üzere sabit kıl", "bize dünyada ve ahirette iyilik ver",
    "bize helal ve bol rızık ihsan eyle", "hastalıklarımıza şifa ver", "bizi salih kullarının arasına kat",
    "ilmimizi ve anlayışımızı artır", "bize sabır ve metanet ver"
]
korunmalar = [
    "bizi cehennem azabından koru", "bizi kabir azabından muhafaza eyle", "bizi şeytanın vesveselerinden koru",
    "bizi görünmez kazalardan ve belalardan esirge", "bizi kötü ahlaktan ve hastalıklardan muhafaza et",
    "bizi zalimlerin şerrinden ve haksızlıklardan koru"
]
kapanislar = [
    "Amin.", "Şüphesiz sen duaları hakkıyla işitensin.", 
    "Sen merhametlilerin en merhametlisisin.", "Dualarımızı dergâh-ı izzetinde kabul eyle."
]

def ana_islem():
    # 1. Kelimeleri birleştirerek yepyeni, özgün bir dua üret
    dua = f"{random.choice(hitaplar)} {random.choice(istekler)}, {random.choice(korunmalar)}. {random.choice(kapanislar)}"
    
    print(f"Günün Duası: {dua}")

    # 2. JSON formatında kaydedilecek veriyi hazırla
    simdi = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    kayit = {
        "son_guncelleme": simdi,
        "gunun_duasi": dua
    }

    # 3. JSON dosyasına yaz (ensure_ascii=False Türkçe karakterlerin düzgün görünmesini sağlar)
    with open('dualar.json', 'w', encoding='utf-8') as f:
        json.dump(kayit, f, ensure_ascii=False, indent=4)
        
    print("Yeni dua üretildi ve dualar.json dosyasına başarıyla kaydedildi.")

if __name__ == "__main__":
    ana_islem()
