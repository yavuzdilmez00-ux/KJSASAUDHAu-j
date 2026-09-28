import os
import json
import random
import google.generativeai as genai

# Gemini API Ayarları (GitHub Secrets'tan alınacak)
API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("GEMINI_API_KEY bulunamadı!")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

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
Sen bir İslam alimi ve edipisin. İslam'a, Kuran'a ve Sünnete tam uygun olacak şekilde "{secilen_konu}" konusunda 15 adet farklı, içten, samimi ve Türkçe dua yaz.
Çıktı SADECE aşağıdaki formatta bir JSON dizisi (array) olmalıdır. Başka hiçbir açıklama veya metin yazma.

[
  {{
    "kategori": "{secilen_konu}",
    "dua": "Rabbimiz! Bize dünyada iyilik ver, ahirette de iyilik ver ve bizi ateş azabından koru."
  }}
]
"""

try:
    # Duaları üret
    response = model.generate_content(prompt)
    ciktı = response.text.strip()
    
    # Markdown (```json ... ```) formatında gelirse temizle
    if ciktı.startswith("```json"):
        ciktı = ciktı[7:-3].strip()
    elif ciktı.startswith("```"):
        ciktı = ciktı[3:-3].strip()

    yeni_dualar = json.loads(ciktı)
    dosya_adi = "dualar.json"
    mevcut_dualar = []

    # Eski duaları oku
    if os.path.exists(dosya_adi):
        with open(dosya_adi, "r", encoding="utf-8") as f:
            try:
                mevcut_dualar = json.load(f)
            except json.JSONDecodeError:
                mevcut_dualar = []

    # Yeni duaları ekle
    mevcut_dualar.extend(yeni_dualar)

    # Dosyaya geri yaz
    with open(dosya_adi, "w", encoding="utf-8") as f:
        json.dump(mevcut_dualar, f, ensure_ascii=False, indent=4)

    print(f"Başarılı! '{secilen_konu}' konusunda {len(yeni_dualar)} dua eklendi. Toplam dua: {len(mevcut_dualar)}")

except Exception as e:
    print(f"Bir hata oluştu: {e}")
