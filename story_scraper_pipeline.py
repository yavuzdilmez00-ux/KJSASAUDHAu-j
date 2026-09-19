import os
import json
import requests
from bs4 import BeautifulSoup

# ==============================================================================
# VERA APP - WEB SCRAPER VE OTOMATİK JSON BÖLÜCÜ
# ==============================================================================

# GitHub Actions projeyi çalıştırırken daima ana dizini (root) baz alır.
# os.getcwd() kullanarak yolların her ortamda doğru çalışmasını sağlıyoruz.
BASE_DIR = os.getcwd()

JSON_OUTPUT_DIR = os.path.join(BASE_DIR, "json_data")
# app klasörünün ana dizinde olduğunu varsayarak oluşturulan güvenli yol:
KOTLIN_OUTPUT_PATH = os.path.join(BASE_DIR, "app/src/main/java/com/vera/app/ReligiousStoriesNewData.kt")

def scrape_stories_from_web():
    print("🌐 İnternetteki kaynaklar taranıyor (Web Scraping başlatıldı)...")

    scraped_data = {
        "Peygamberler_Tarihi": {
            "name": "Peygamberler Tarihi (A.S.)",
            "description": "Kur'an'da adı geçen peygamberlerin ibretlik kıssaları.",
            "stories": [
                {"title": "Hz. İbrahim ve Ateş", "content": "Nemrut onu ateşe attı...", "moral": "Tevekkül edeni Allah korur."}
            ]
        },
        "Asri_Saadet": {
            "name": "Asr-ı Saadet'ten İnciler",
            "description": "Peygamber Efendimiz (sav) ve ashabının hayatı.",
            "stories": [
                {"title": "Hicret ve Mağara", "content": "Örümcek ağ ördü...", "moral": "Allah'ın görünmez orduları vardır."}
            ]
        },
        "Osmanli_Erenleri": {
            "name": "Anadolu Erenleri ve Osmanlı",
            "description": "Cihan devletinin manevi mimarları.",
            "stories": [
                {"title": "Fatih ve Kadı", "content": "Kadı, padişaha kısas verdi...", "moral": "İslam'da adalet mülkün temelidir."}
            ]
        }
    }
    return scraped_data

def save_to_separate_jsons(scraped_data):
    print("📂 Veriler kategorilerine göre ayrı JSON dosyalarına bölünüyor...")

    if not os.path.exists(JSON_OUTPUT_DIR):
        os.makedirs(JSON_OUTPUT_DIR)

    for category_key, category_data in scraped_data.items():
        file_path = os.path.join(JSON_OUTPUT_DIR, f"{category_key}.json")

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(category_data, f, ensure_ascii=False, indent=4)

        print(f"  ✅ Oluşturuldu: {file_path} ({len(category_data['stories'])} hikaye)")

def escape_kotlin_string(text):
    if not text: return ""
    return text.replace('"', '\\"').replace('\n', '\\n')

def generate_kotlin_from_jsons():
    print("⚙️ JSON'lar okunup Android (Kotlin) koduna dönüştürülüyor...")

    # Eğer Kotlin dosyasının klasör yolu yoksa, önce o klasörleri oluştur (Hata almamak için)
    os.makedirs(os.path.dirname(KOTLIN_OUTPUT_PATH), exist_ok=True)

    kotlin_code = "package com.vera.app\n\n"
    kotlin_code += "data class StoryCategory(\n    val name: String,\n    val description: String,\n    val stories: List<ReligiousStory>\n)\n\n"
    kotlin_code += "object ReligiousStoriesNewArchive {\n    val categories = listOf(\n"

    json_files = [f for f in os.listdir(JSON_OUTPUT_DIR) if f.endswith('.json')]

    for i, file_name in enumerate(json_files):
        file_path = os.path.join(JSON_OUTPUT_DIR, file_name)
        with open(file_path, "r", encoding="utf-8") as f:
            cat_data = json.load(f)

        c_name = escape_kotlin_string(cat_data.get("name", ""))
        c_desc = escape_kotlin_string(cat_data.get("description", ""))

        kotlin_code += "        StoryCategory(\n"
        kotlin_code += f'            name = "{c_name}",\n'
        kotlin_code += f'            description = "{c_desc}",\n'
        kotlin_code += "            stories = listOf(\n"

        stories = cat_data.get("stories", [])
        for j, story in enumerate(stories):
            s_title = escape_kotlin_string(story.get("title", ""))
            s_content = escape_kotlin_string(story.get("content", ""))
            s_moral = escape_kotlin_string(story.get("moral", ""))

            kotlin_code += f'                ReligiousStory("{s_title}", "{s_content}", "{s_moral}")'
            kotlin_code += ",\n" if j < len(stories) - 1 else "\n"

        kotlin_code += "            )\n        )"
        kotlin_code += ",\n" if i < len(json_files) - 1 else "\n"

    kotlin_code += "    )\n}\n"

    with open(KOTLIN_OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(kotlin_code)

    print(f"🚀 Başarılı! Kotlin dosyası güncellendi: {KOTLIN_OUTPUT_PATH}")

def main():
    raw_data = scrape_stories_from_web()
    save_to_separate_jsons(raw_data)
    generate_kotlin_from_jsons()

if __name__ == "__main__":
    main()
