import time, json
from urllib3 import PoolManager

from constant import *


NTFY_ENDPOINT = "https://ntfy.sh/{}"
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"
OWM_ICON_PATH = "https://openweathermap.org/img/wn/{}@2x.png"
http = PoolManager()


def get_current_weather(appid: str, lat: str, lon: str) -> int:
    response = http.request(
        "GET",
        OWM_ENDPOINT,
        fields={"lat": lat, "lon": lon, "appid": appid, "units": "metric"},
    )

    return json.loads(response.data.decode("utf-8"))


def send_notification(title: str, message: str, icon: str, priority: str) -> None:
    for topic in NTFY_TOPICS:
        http.request(
            "POST",
            NTFY_ENDPOINT.format(topic),
            body=message,
            headers={"Title": title, "Icon": icon, "Priority": priority},
        )


def format_message(data: dict) -> str:
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    suggestion = SUGGESTIONS.get(data["weather"][0]["id"])

    return NTFY_MESSAGE_TEMPLATE.format(
        suggestion, temp, feels_like, humidity,
    ).encode("utf-8")


if __name__ == "__main__":
    start_time = time.time()

    data = get_current_weather(OWM_APPID, OWM_LAT, OWM_LON)
    icon = OWM_ICON_PATH.format(data["weather"][0]["icon"])
    send_notification(NTFY_TITLE, format_message(data), icon, NTFY_PRIORITY)

    print("Finished in {} seconds".format(round(time.time() - start_time, 1)))
