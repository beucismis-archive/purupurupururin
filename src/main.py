import time, json
from urllib3 import PoolManager

from constant import *


NTFY_ENDPOINT = "ntfy.sh/{}"
OWM_ENDPOINT = "api.openweathermap.org/data/2.5/weather"
http = PoolManager()


def get_weather_id(lat: str, lon: str, appid: str) -> int:
    response = http.request(
        "GET",
        OWM_ENDPOINT,
        fields={"lat": lat, "lon": lon, "appid": appid},
    )
    data = json.loads(response.data.decode("utf-8"))

    return data["weather"][0]["id"]


def send_notification(title: str, message: str) -> None:
    for topic in NTFY_TOPICS:
        response = http.request(
            "POST",
            NTFY_ENDPOINT.format(topic),
            body=message,
            headers={"Title": title, "Priority": NTFY_PRIORITY},
        )


if __name__ == "__main__":
    start_time = time.time()

    weather_id = get_weather_id(OWM_LAT, OWM_LON, OWM_APPID)
    message = SUGGESTIONS.get(weather_id).encode("utf-8")
    send_notification(title=NTFY_TITLE, zessage=message)

    print("Finished in {} seconds".format(round(time.time() - start_time, 1)))
