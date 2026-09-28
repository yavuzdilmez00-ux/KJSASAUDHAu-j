import os
import sys
import json
import time
import random
import urllib.request

# Duaların üretileceği kategoriler
konular = [
    "Şükür ve Hamd", "Sağlık ve Şifa", "Rızık ve Bereket", 
    "Sıkıntı ve Kederden Kurtuluş", "Bağışlanma ve Tövbe", 
    "Aile ve Çocuklar", "Sınav ve Başarı", "Ahiret ve Cennet",
    "Sabır ve İrade", "Kaza ve Beladan Korunma"
]
secilen_konu = random.choice(konular)

prompt = f"""
İslam'a, Kuran'a ve Sünnete tam uygun olacak şekilde "{secilen_konu}" konusunda 10 adet farklı, içten ve Türkçe dua yaz.
Çıktı SADECE aşağıdaki formatta bir JSON dizisi (array) olmalıdır. Başka hiçbir metin, giriş veya sonuç cümlesi yazma:

[
  {{
    "kategori": "{secilen_konu}",
    "dua": "Rabbimiz! Bize dünyada iyilik ver, ahirette de iyilik ver ve bizi ateş azabından koru."
  }}
]
"""

dosya_adi = "dualar.json"

# Dosya yoksa oluştur (Git çökmesini engeller)
if not os.path.exists(dosya_adi):
    with open(dosya_adi, "w", encoding="utf-8") as f:
        json.dump([], f)

try:
    print("Yapay zekaya bağlanılıyor (API Key ve Tarayıcı gerektirmez)...")
    
    # Tamamen ücretsiz, açık ve şifresiz metin AI ağını kullanıyoruz
    url = "https://text.pollinations.ai/"
    payload = json.dumps({
        "messages": [
            {"role": "system", "content": "Sen bir İslam alimi ve edipisin. Çıktıların SADECE geçerli bir JSON formatında olmalıdır."},
            {"role": "user", "content": prompt}
        ],
        "jsonMode": True
    }).encode("utf-8")

    headers = {'Content-Type': 'application/json'}
    req = urllib.request.Request(url, data=payload, headers=headers)

    ciktı = ""
    for deneme in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as response:
                ciktı = response.read().decode('utf-8')
                if ciktı:
                    break
        except Exception as e:
            print(f"{deneme + 1}. deneme başarısız oldu: {e}")
            time.sleep(5)
            
    if not ciktı:
        print("Yapay zeka sunucusundan yanıt alınamadı. İşlem sessizce atlanıyor.")
        sys.exit(0)

    # Gelen yanıtı JSON formatına temizle
    ciktı = ciktı.strip()
    if ciktı.startswith("```json"):
        ciktı = ciktı[7:-3].strip()
    elif ciktı.startswith("```"):
        ciktı = ciktı[3:-3].strip()

    try:
        yeni_dualar = json.loads(ciktı)
    except json.JSONDecodeError:
        print("Gelen yanıt geçerli bir JSON değil. İşlem sessizce atlanıyor.")
        sys.exit(0)

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
