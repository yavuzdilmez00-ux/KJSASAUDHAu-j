package com.vera.app

data class StoryCategory(
    val name: String,
    val description: String,
    val stories: List<ReligiousStory>
)

object ReligiousStoriesNewArchive {
    val categories = listOf(
        StoryCategory(
            name = "Asr-ı Saadet'ten İnciler",
            description = "Peygamber Efendimiz (sav) ve ashabının hayatı.",
            stories = listOf(
                ReligiousStory("Hicret ve Mağara", "Örümcek ağ ördü...", "Allah'ın görünmez orduları vardır.")
            )
        ),
        StoryCategory(
            name = "Anadolu Erenleri ve Osmanlı",
            description = "Cihan devletinin manevi mimarları.",
            stories = listOf(
                ReligiousStory("Fatih ve Kadı", "Kadı, padişaha kısas verdi...", "İslam'da adalet mülkün temelidir.")
            )
        ),
        StoryCategory(
            name = "Peygamberler Tarihi (A.S.)",
            description = "Kur'an'da adı geçen peygamberlerin ibretlik kıssaları.",
            stories = listOf(
                ReligiousStory("Hz. İbrahim ve Ateş", "Nemrut onu ateşe attı...", "Tevekkül edeni Allah korur.")
            )
        )
    )
}
