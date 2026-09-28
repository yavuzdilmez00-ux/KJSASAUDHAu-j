import yaml
import random
from datetime import datetime

DOSYA_YOLU = 'dualar.yml'

def ana_islem():
    # 1. Dosyayı Oku
    try:
        with open(DOSYA_YOLU, 'r', encoding='utf-8') as f:
            veri = yaml.safe_load(f) or {}
    except FileNotFoundError:
        veri = {'dualar': {'genel': ["Allah'ım bize merhamet et."]}}

    # 2. Rastgele bir dua seç
    dualar = veri.get('dualar', {})
    tum_dualar = []
    for kategori, dua_listesi in dualar.items():
        if isinstance(dua_listesi, list):
            tum_dualar.extend(dua_listesi)
            
    if not tum_dualar:
        print("Okunacak dua bulunamadı.")
        return

    secilen_dua = random.choice(tum_dualar)
    print(f"Günün Duası: {secilen_dua}")

    # 3. YAZMA İŞLEMİ: Dosyayı güncelle (GitHub'a pushlanacak kısım)
    simdi = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # meta verilerini güncelle
    if 'meta' not in veri:
        veri['meta'] = {}
    
    veri['meta']['son_calisma_tarihi'] = simdi
    veri['meta']['son_okunan_dua'] = secilen_dua

    # 4. Dosyaya geri yaz (allow_unicode=True Türkçe karakterleri bozmamak için önemli)
    with open(DOSYA_YOLU, 'w', encoding='utf-8') as f:
        yaml.dump(veri, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
        
    print("dualar.yml başarıyla güncellendi ve kaydedildi.")

if __name__ == "__main__":
    ana_islem()
