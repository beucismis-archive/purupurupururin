import os

from dotenv import load_dotenv


load_dotenv()

# https://openweathermap.org/api/geocoding-api
LATITUDE: str = os.getenv("LATITUDE")
LONGITUDE: str = os.getenv("LONGITUDE")

# https://docs.ntfy.sh/publish
NTFY_API_ENDPOINT: str = "https://ntfy.sh"
# https://openweathermap.org/current
OWM_API_ENDPOINT: str = "https://api.openweathermap.org/data/2.5/weather"
# https://openweathermap.org/weather-conditions#How-to-get-icon-URL
OWM_ICON_ENDPOINT: str = "https://openweathermap.org/img/wn/{}@2x.png"

# https://home.openweathermap.org/api_keys
OWM_API_KEY: str = os.getenv("OWM_API_KEY")
# https://openweathermap.org/current#data
OWM_UNITS: str = "metric"

# https://docs.ntfy.sh/publish/#message-priority
NTFY_PRIORITY: int = 3
# https://docs.ntfy.sh/faq/?h=topic#what-happens-if-there-are-multiple-subscribers-to-the-same-topic
NTFY_TOPIC: str = os.getenv("NTFY_TOPIC")

NOTIFICATION_TITLE: str = "Dışarı mı çıksam?"
# Formats: suggestion, temp, feels_like, humidity
NOTIFICATION_MESSAGE_TEMPLATE: str = "{}\nDeğerler: Sıcaklık: {} °C - Hissedilen: {} °C - Nem: %{}"

# http://www.openweathermap.org/weather-conditions#Weather-Condition-Codes-2
WEATHER_SUGGESTIONS: dict = {
    200: "Şimşekler göğü yırtıyor, gök gürüldüyor! Hala dışarı çıkmayı düşünüyorsun?",
    201: "Fırtına kopuyor, gök gürüldü! Cesaretin var mı dışarı çıkmaya?",
    202: "Şimşekler arka arkaya çakıyor! Dışarıda olmanın akıllıca olduğunu mu düşünüyorsun?",
    210: "Havanın öfkesiyle mücadele etmek mi? Şimşek çakıyor, gök gürüldü, dur bir düşün!",
    211: "Şimşekler, fırtına derken dışarı çıkmak sana ne kazandıracak ki?",
    212: "Fırtına patlak verdi! Dışarı çıkma, güvenli alanda kal.",
    221: "Gök gürlüyor, şimşekler çakıyor. Hala dışarıda olma kararı mı aldın?",
    230: "Fırtına başlamış, gök gürüldü! Bence evde kalmak en iyisi.",
    231: "Şimşekler göz kırpıyor, gök gürlüyor. Dışarıda ne işin var?",
    232: "Korkusuzca dışarıda mı olacaksın? Gök gürlüyor ve şimşekler çakıyor!",
    300: "Yağmurun sesi bile evde olmak için bir bahane! Dışarı çıkma, dizi izle.",
    301: "Havanın yağmurlu hali sana 'Evde kal' demek için fazlasıyla yeterli!",
    302: "Yağmur demek evde rahat bir zaman demek! Bir film aç ve dışarıyı unut.",
    310: "Yağmur sağanak yağıyor. Dışarıda olmak yerine evde takıl.",
    311: "Yağmur fışkırıyor! Evde kal, keyfini çıkar.",
    312: "Ağır yağmur var. Evde film maratonu yapmanın tam zamanı!",
    313: "Dışarıda resmen gökyüzü boşanıyor. Evde kalıp rahat et.",
    314: "Yağmur sağanak halinde. Dışarı çıkmak neye yarar ki?",
    321: "Yağmurun ritmini evde dinle, dışarıya çıkma.",
    500: "Yağmur hafif. Biraz dışarı çıkıp suyun tadını çıkar, sonra sıcak bir kahve iç!",
    501: "Yağmur hafif, ama soğuk! Biraz yürüyüş yapabilirsin, ama dikkat et.",
    502: "Yağmur var ama dışarıda kalmak yerine evde güzel bir kitap okuman gerek.",
    503: "Yağmur yağıyor, ama bu seni evde tutamaz! Yağmurun altına çıkıp rahatlayabilirsin.",
    504: "Yağmur iyice bastırmış, ama belki senin için bir yürüyüş fena olmaz.",
    511: "Dışarıda deli gibi yağmur yağıyor! Bunu görmüyor musun?",
    520: "Yağmur var, ama seni evde tutmaya yetecek kadar yoğun.",
    521: "Yağmur var, evde otur, dışarıya çıkmaya değmez.",
    522: "Yağmur var, sabırlı ol, dışarıya çıkma.",
    531: "Hava kar yağıyor, sen de içindeki yağmuru hisset.",
    600: "Dışarıda hafif kar var. Çıkıp biraz karın tadını çıkar, ama fazla uzun kalma.",
    601: "Dışarıda hafif bir kar var. Biraz dışarıda dolaş, ama dikkatli ol!",
    602: "Kar çok ağır, sanki gökyüzü bile düşmeye çalışıyor! Biraz daha içeriye git.",
    611: "Karla karışık yağmur var. Dışarıda olmak, sadece kirli ayakkabılara sebep olur!",
    612: "Karla karışık yağmur var. Dışarı çıkma, ayakkabıların çamur içinde kalacak.",
    615: "Karla karışık yağmur? Hadi, senin yerine ben evde kalıyorum.",
    616: "Karla karışık yağmur. Çıkıp bir şey kirletmene gerek yok, otur evde.",
    620: "Dışarıda kar var, hadi gel, biraz eğlen!",
    621: "Hava karlı, ama dışarıda hiçbir şey yapmanın anlamı yok.",
    622: "Dışarıda karlık bir dünya var. Soğuk ama muazzam bir atmosfer.",
    701: "Sis var, gözün hiç bir şey görmüyor. Ama belki sisin içinde kaybolmak istersin?",
    711: "Sis, tam bir gizem havası var! Dışarıda bir şeyler keşfetmeye ne dersin?",
    721: "Sis var, dışarıda bir şey görmüyor olabilirsin ama atmosfer bir harika.",
    731: "Kum fırtınası! Dışarı çıkmaya cesaretin var mı? Hadi bakalım.",
    741: "Sis var, ama gizemi çözmeye hazır mısın? Biraz dışarıda zaman geçir.",
    751: "Kum fırtınası, dışarıda hayatta kalmak için hazır mısın?",
    761: "Volkanik kül! Dışarıda macera var ama sana önerim durman.",
    771: "Sinirli bir hava, stresli bir atmosfer. Evde bir kahve yap, rahatla.",
    781: "TORNADO! Eğer hayatını biraz heyecanlı yaşamak istiyorsan, dışarı çık.",
    800: "Hava muazzam! Her şey parlak ve temiz. Dışarıda olmanın tam zamanı.",
    801: "Biraz bulut var ama ne gam? Hadi dışarı çık, güneşin tadını çıkar.",
    802: "Hava bulutlu, ama yine de dışarıda zaman geçirmek için mükemmel bir gün.",
    803: "Bulutlar var, ama dışarı çıkıp gezmek için hala harika bir gün!",
    804: "Hava bulutlu, ama dışarıda olmak için mükemmel bir fırsat. Hadi, git ve keşfet!",
}
