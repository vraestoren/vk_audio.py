# vk_audio.py
Web-API for interacting with audios in [vkontakte](https://vk.com) social network

## Example
```python3
import vk_audio
vk_audio = vk_audio.VkAudio(access_token="")
popular_audios = vk_audio.get_popular_audios()
print(popular_audios)
```
