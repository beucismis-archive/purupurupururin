# purupurupururin
Gives you advice on going out on the weather (Uses [OpenWeatherMap](https://openweathermap.org) to get current weather data). It does this by sending notifications to your phone or desktop using [ntfy](https://ntfy.sh). No need to run it on your local computer or on a server. It can run at scheduled times with the GitHub workflow. All you have to do is clone the repository and set the secret environment variables.

### Environment Variables

Go to path `Repository` > `Settings` > `Secrets` > `Actions` > `New repository secret` to set the repository environments.

| Key | Type | Description |
| - | - | - |
| `OWM_LAT` | `str` | Your latitude coordinates |
| `OWM_LON` | `str` | Your longitude coordinates |
| `OWM_APPID` | `str` | Your unique API key (https://home.openweathermap.org/api_keys) |
| `NTFY_TOPICS` | `list` | Your subscribed topic names list (E.g: `["mytopic"]`) |

## Credits and References

Suggestion messages were inspired by [halilkaya/disari-mi-ciksam](https://github.com/halilkaya/disari-mi-ciksam) project.

## License

This project is licensed under the GPL-3.0 - see the LICENSE file for details.