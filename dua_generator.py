import os
import sys
import json
import time
import random
from duckduckgo_search import DDGS

# Duaların üretileceği kategoriler
konular = [
    "Şükür ve Hamd", "Sağlık ve Şifa", "Rızık ve Bereket", 
    "Sıkıntı ve Kederden Kurtuluş", "Bağışlanma ve Tövbe", 
    "Aile ve Çocuklar", "Sınav ve Başarı", "Ahiret ve Cennet",
    "Sabır ve İrade", "Kaza ve Beladan Korunma"
]
secilen_konu = random.choice(konular)

# Yapay zekaya verilecek kesin komut
prompt = f"""
Sen bir İslam alimi ve edipisin. İslam'a, Kuran'a ve Sünnete tam uygun olacak şekilde "{secilen_konu}" konusunda 10 adet farklı, içten, samimi ve Türkçe dua yaz.
Çıktı SADECE aşağıdaki formatta bir JSON dizisi (array) olmalıdır. Başka hiçbir açıklama, giriş veya sonuç cümlesi yazma. Sadece JSON kodunu ver.

[
  {{
    "kategori": "{secilen_konu}",
    "dua": "Rabbimiz! Bize dünyada iyilik ver, ahirette de iyilik ver ve bizi ateş azabından koru."
  }}
]
"""

dosya_adi = "dualar.json"

# Eğer dosya hiç yoksa, Git'in çökmemesi için boş bir liste oluştur
if not os.path.exists(dosya_adi):
    with open(dosya_adi, "w", encoding="utf-8") as f:
        json.dump([], f)

try:
    print("Yapay zekaya bağlanılıyor (API gerektirmez)...")
    
    # Sunucu anlık hata verebilir diye 3 kez tekrar deneme (retry) sistemi kuruyoruz
    ciktı = ""
    for deneme in range(3):
        try:
            ciktı = DDGS().chat(prompt, model="gpt-4o-mini")
            if ciktı:
                break
        except Exception as e:
            print(f"{deneme + 1}. deneme başarısız oldu: {e}")
            time.sleep(5) # 5 saniye bekleyip tekrar dene
            
    if not ciktı:
        print("Yapay zeka sunucusundan yanıt alınamadı. İşlem iptal ediliyor.")
        sys.exit(0) # Hata vermeden sessizce durdur ki Git çökmesin

    # Gelen yanıtı temizle
    ciktı = ciktı.strip()
    if ciktı.startswith("```json"):
        ciktı = ciktı[7:-3].strip()
    elif ciktı.startswith("```"):
        ciktı = ciktı[3:-3].strip()

    yeni_dualar = json.loads(ciktı)
    mevcut_dualar = []

    # Eski duaları oku
    with open(dosya_adi, "r", encoding="utf-8") as f:
        try:
            mevcut_dualar = json.load(f)
        except json.JSONDecodeError:
            mevcut_dualar = []

    # Yeni duaları mevcut listeye ekle
    mevcut_dualar.extend(yeni_dualar)

    # Dosyaya geri yaz
    with open(dosya_adi, "w", encoding="utf-8") as f:
        json.dump(mevcut_dualar, f, ensure_ascii=False, indent=4)

    print(f"Başarılı! '{secilen_konu}' konusunda {len(yeni_dualar)} dua eklendi. Toplam dua sayısı: {len(mevcut_dualar)}")

except Exception as e:
    print(f"Kritik bir hata oluştu: {e}")
    sys.exit(0)
