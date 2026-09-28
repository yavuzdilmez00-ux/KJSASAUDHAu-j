import yaml
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
    # 1. Kelimeleri birleştirerek anında yepyeni, özgün bir dua üret
    dua = f"{random.choice(hitaplar)} {random.choice(istekler)}, {random.choice(korunmalar)}. {random.choice(kapanislar)}"
    
    print(f"Günün Duası: {dua}")

    # 2. Üretilen duayı GitHub'a kaydetmek için YML verisi hazırla
    simdi = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    kayit = {
        "son_guncelleme": simdi,
        "gunun_duasi": dua
    }

    # 3. YML dosyasının üzerine yaz (Actions bunu GitHub'a pushlayacak)
    with open('dualar.yml', 'w', encoding='utf-8') as f:
        yaml.dump(kayit, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
        
    print("Yeni dua üretildi ve dualar.yml dosyasına başarıyla kaydedildi.")

if __name__ == "__main__":
    ana_islem()
