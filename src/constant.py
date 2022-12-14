import json
from os import environ


# https://openweathermap.org/current

OWM_LAT = environ.get("OWM_LAT")
OWM_LON = environ.get("OWM_LON")
OWM_APPID = environ.get("OWM_APPID")

# https://docs.ntfy.sh/publish

NTFY_PRIORITY = "5"
NTFY_TOPICS = json.loads(environ.get("NTFY_TOPICS"))
NTFY_TITLE = "Dışarı mı çıksam?".encode("utf-8")
NTFY_MESSAGE_TEMPLATE = "{}\nSıcaklık: {}°C   Hissedilen: {}°C   Nem: %{}"

# http://www.openweathermap.org/weather-conditions#Weather-Condition-Codes-2

SUGGESTIONS = {
    200: "Şimşek çakıyor, gök gürüldüyor. Hala dışarı çıkmayı mı düşünüyorsun?",
    201: "Şimşek çakıyor, gök gürüldüyor. Hala dışarı çıkmayı mı düşünüyorsun?",
    202: "Şimşek çakıyor, gök gürüldüyor. Hala dışarı çıkmayı mı düşünüyorsun?",
    210: "Şimşek çakıyor, gök gürüldüyor. Hala dışarı çıkmayı mı düşünüyorsun?",
    211: "Şimşek çakıyor, gök gürüldüyor. Hala dışarı çıkmayı mı düşünüyorsun?",
    212: "Şimşek çakıyor, gök gürüldüyor. Hala dışarı çıkmayı mı düşünüyorsun?",
    221: "Şimşek çakıyor, gök gürüldüyor. Hala dışarı çıkmayı mı düşünüyorsun?",
    230: "Şimşek çakıyor, gök gürüldüyor. Hala dışarı çıkmayı mı düşünüyorsun?",
    231: "Şimşek çakıyor, gök gürüldüyor. Hala dışarı çıkmayı mı düşünüyorsun?",
    232: "Şimşek çakıyor, gök gürüldüyor. Hala dışarı çıkmayı mı düşünüyorsun?",
    300: "Hava çok yağmurlu ya. Otur evde dizi seyret, çıkma dışarı.",
    301: "Hava çok yağmurlu ya. Otur evde dizi seyret, çıkma dışarı.",
    302: "Hava çok yağmurlu ya. Otur evde dizi seyret, çıkma dışarı.",
    310: "Hava çok yağmurlu ya. Otur evde dizi seyret, çıkma dışarı.",
    311: "Hava çok yağmurlu ya. Otur evde dizi seyret, çıkma dışarı.",
    312: "Hava çok yağmurlu ya. Otur evde dizi seyret, çıkma dışarı.",
    313: "Hava çok yağmurlu ya. Otur evde dizi seyret, çıkma dışarı.",
    314: "Hava çok yağmurlu ya. Otur evde dizi seyret, çıkma dışarı.",
    321: "Hava çok yağmurlu ya. Otur evde dizi seyret, çıkma dışarı.",
    500: "Hava hafif yağmurlu. Biraz çıkıp yağmurun altında yürüyebilirsin aslında.",
    501: "Hava hafif yağmurlu. Biraz çıkıp yağmurun altında yürüyebilirsin aslında.",
    502: "Hava baya yağmurlu. İstersen evde oturup yağmuru seyret.",
    503: "Hava baya yağmurlu. İstersen evde oturup yağmuru seyret.",
    504: "Hava baya yağmurlu. İstersen evde oturup yağmuru seyret.",
    511: "Ne işin var dışarıda? Deli gibi yağmur yağıyor, görmüyor musun?",
    520: "Hava yağmurlu ya. Bugün çıkma bence hiç.",
    521: "Hava yağmurlu ya. Bugün çıkma bence hiç.",
    522: "Hava yağmurlu ya. Bugün çıkma bence hiç.",
    531: "Dışarıda kar yağıyor benim içime yağmur.mp3",
    600: "Dışarıda hafif bi kar var. İstersen çık biraz, tadını çıkar.",
    601: "Dışarıda hafif bi kar var. İstersen çık biraz, tadını çıkar.",
    602: "Hava kurşun gibi ağır!",
    611: "Off! Karla karışık yağmur. Çıkıp ayakkabını, pantolonunu kirlettiğine değmez.",
    612: "Off! Karla karışık yağmur. Çıkıp ayakkabını, pantolonunu kirlettiğine değmez.",
    615: "Off! Karla karışık yağmur. Çıkıp ayakkabını, pantolonunu kirlettiğine değmez.",
    616: "Off! Karla karışık yağmur. Çıkıp ayakkabını, pantolonunu kirlettiğine değmez.",
    620: "Dışarıda hafif bi kar var. İstersen çık biraz, tadını çıkar.",
    621: "Hava karlı ya. Otur oturduğun yerde.",
    622: "Dışarısı buz gibi lapa lapa kar var benim içim yanıyor...",
    701: "Hava sisli. İstersen çık bi bak bakalım. Güzel bi atmosfer vardır.",
    711: "Hava sisli. İstersen çık bi bak bakalım. Güzel bi atmosfer vardır.",
    721: "Hava sisli. İstersen çık bi bak bakalım. Güzel bi atmosfer vardır.",
    731: "Oo! Hacı kapat kapıyı pencereyi, otur evde. Kum fırtasını var kum!",
    741: "Hava sisli. İstersen çık bi bak bakalım. Güzel bi atmosfer vardır.",
    751: "Oo! Hacı kapat kapıyı pencereyi, otur evde. Kum fırtasını var kum!",
    761: "Volkanik kül hacı! Ben daha birşey demiyorum.",
    771: "Dışarısı sinir stres. Evde otur, bi kahve yap bence.",
    781: "TORNADO! Hadi... :D",
    800: "Hava çok güzel. Evde oturup napcan? Hadi, dışarı çık.",
    801: "Hava biraz bulutlu ama güzel yine de. Hadi, dışarı çık.",
    802: "Hava biraz bulutlu ama güzel yine de. Hadi, dışarı çık.",
    803: "Hava biraz bulutlu ama güzel yine de. Hadi, dışarı çık.",
    804: "Hava biraz bulutlu ama güzel yine de. Hadi, dışarı çık.",
}
