# purupurupururin

Gives you advice on going out on the weather. Uses OpenWeather to get current weather data and It this sending notification to your phone or desktop using [ntfy](https://ntfy.sh). No need to deploy it on your local computer or on a server. It can run at [scheduled](https://github.com/beucismis-archive/purupurupururin/blob/main/.github/workflows/main.yml#L7) times with the GitHub workflow. All you have to do is clone the repository and set the secret environment variables.

![purupurupururin-screenshot](https://user-images.githubusercontent.com/40023234/205644044-b90da712-4851-4d44-8b29-a24284c253c6.jpg)

### Environment Variables

| Key | Type | Description |
| - | - | - |
| `OWM_LAT` | `str` | Your latitude coordinates |
| `OWM_LON` | `str` | Your longitude coordinates |
| `OWM_APPID` | `str` | Your unique [API](https://home.openweathermap.org/api_keys) key |
| `NTFY_TOPICS` | `list` | Your subscribed topic names list |

Go to path `Repository` > `Settings` > `Secrets` > `Actions` > `New repository secret` to set the repository environments.

## Credits and References

- Mobil and desktop client setup from https://docs.ntfy.sh
- Current weather data api docs from https://openweathermap.org/current
- Suggestion messages were inspired by [halilkaya/disari-mi-ciksam](https://github.com/halilkaya/disari-mi-ciksam) project.

## License

This project is licensed under the GPL-3.0 - see the LICENSE file for details.
