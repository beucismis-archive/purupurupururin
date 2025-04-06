import time
import json

import requests

from constant import *


def get_current_weather(api_key: str, latitude: str, longitude: str, units: str) -> dict:
    response = requests.get(
        OWM_API_ENDPOINT,
        params={"appid": api_key, "lat": latitude, "lon": longitude, "units": units},
    )

    return response.json()


def send_notification(
    topic: str, title: str, message: str, icon: str, priority: int
) -> None:
    requests.post(
        NTFY_API_ENDPOINT,
        data=json.dumps(
            {
                "topic": topic,
                "title": title,
                "message": message,
                "icon": icon,
                "priority": priority,
            }
        ),
    )


def format_message(data: dict) -> str:
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    suggestion = WEATHER_SUGGESTIONS.get(data["weather"][0]["id"])

    return NOTIFICATION_MESSAGE_TEMPLATE.format(
        suggestion,
        temp,
        feels_like,
        humidity,
    )


if __name__ == "__main__":
    start_time = time.time()

    current_weather = get_current_weather(OWM_API_KEY, LATITUDE, LONGITUDE, OWM_UNITS)
    weather_icon = OWM_ICON_ENDPOINT.format(current_weather["weather"][0]["icon"])
    message = format_message(current_weather)

    send_notification(
        NTFY_TOPIC, NOTIFICATION_TITLE, message, weather_icon, NTFY_PRIORITY
    )

    print("Finished in {} seconds".format(round(time.time() - start_time, 1)))
