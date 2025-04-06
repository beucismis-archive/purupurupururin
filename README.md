# purupurupururin

Gives you advice on going out on the weather. Uses OpenWeather to get current weather data and It this sending notification to your phone or desktop using [ntfy](https://ntfy.sh). No need to deploy it on your local computer or on a server. It can run at [scheduled](https://github.com/beucismis-archive/purupurupururin/blob/main/.github/workflows/main.yml#L7) times with the GitHub workflow. All you have to do is clone the repository and set the secret environment variables.

![screenshot](https://github.com/user-attachments/assets/051c7b06-946f-4f1d-89a6-d00f796285e1)

### Environment Variables

| Key | Type | Description |
| - | - | - |
| `LATITUDE` | `str` | Your latitude coordinates |
| `LONGITUDE` | `str` | Your longitude coordinates |
| `OWM_API_KEY` | `str` | Your unique [API](https://home.openweathermap.org/api_keys) key |
| `NTFY_TOPIC` | `str` | Your subscribed topic name |

Go to path `Repository` > `Settings` > `Secrets and variables` > `Actions` > `Secrets` > `Repository secrets` > `New repository secret` to set the repository environments.

## Credits and References

Suggestion messages were inspired by [halilkaya/disari-mi-ciksam](https://github.com/halilkaya/disari-mi-ciksam) project.

## License

This project is licensed under the GPL-3.0 - see the LICENSE file for details.
