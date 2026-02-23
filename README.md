# vk_audio.py

> Web-API for [VKontakte](https://vk.com) Audio API to search, manage, and organise music in VK programmatically

---

## Quick Start

```python
from vk_audio import VkAudio

vk_audio = VkAudio(access_token="your_token_here")

# Get popular tracks
popular = vk_audio.get_popular_audios()
print(popular)
```

---

## Features

- 🎵 **Audio** — get, add, delete, edit, reorder tracks
- 🔍 **Search** — search tracks, albums, artists, and playlists
- 🎤 **Artists** — get artist info, albums, and tracks by artist
- 📋 **Playlists** — create, delete, follow, and manage playlist contents
- ⭐ **Recommendations** — suggested and popular tracks

---

## Usage

### Audio

```python
# Get all tracks for a user or group
vk_audio.get_audio(owner_id=123456)

# Get a specific track by its composite ID (owner_id_audio_id)
vk_audio.get_audio_by_id(audio_ids="123456_789")

# Get total track count for an owner
vk_audio.get_audios_count(owner_id=123456)

# Get lyrics
vk_audio.get_lyrics_for_audio(lyrics_id=9876)

# Add a track to your library
vk_audio.add_audio(owner_id=123456, audio_id=789)

# Delete a track
vk_audio.delete_audio(owner_id=123456, audio_id=789)

# Edit track metadata
vk_audio.edit_audio(owner_id=123456, audio_id=789, artist="Artist", title="Title")

# Reorder a track (move it before another)
vk_audio.reorder_audio(owner_id=123456, audio_id=789, before_audio_id=790)

# Popular tracks
vk_audio.get_popular_audios(count=20)

# Suggested tracks for a user
vk_audio.get_suggested_audios(target_id="123456", count=10)
```

### Search

```python
vk_audio.search_audio(query="Radiohead", count=10)
vk_audio.search_albums(query="OK Computer")
vk_audio.search_artists(query="Radiohead")
vk_audio.search_playlists(query="chill", filters="albums")
```

### Artists

```python
# Get artist profile
vk_audio.get_artist_by_id(artist_id=123)

# Get an artist's albums
vk_audio.get_albums_by_artist(artist_id=123, count=5)

# Get an artist's tracks
vk_audio.get_audios_by_artist(artist_id=123, count=20)
```

### Playlists

```python
# Get all playlists for a user
vk_audio.get_playlists(owner_id=123456)

# Get a specific playlist
vk_audio.get_playlist_by_id(owner_id=123456, playlist_id=1, access_key=0)

# Create a playlist
vk_audio.create_playlist(owner_id=123456, title="My Playlist")

# Delete a playlist
vk_audio.delete_playlist(owner_id=123456, playlist_id=1)

# Follow a playlist
vk_audio.follow_playlist(owner_id=123456, playlist_id=1)

# Add tracks to a playlist (comma-separated IDs)
vk_audio.add_audio_to_playlist(owner_id=123456, playlist_id=1, audio_ids="123_456,123_457")

# Remove tracks from a playlist
vk_audio.remove_audios_from_playlist(owner_id=123456, playlist_id=1, audio_ids="123_456")
```

---

## API Reference

| Method                        | Description                                  |
|-------------------------------|----------------------------------------------|
| `get_audio`                   | Get tracks for an owner                      |
| `get_audio_by_id`             | Get specific tracks by ID                    |
| `get_audios_count`            | Get total track count for an owner           |
| `get_lyrics_for_audio`        | Get lyrics by lyrics ID                      |
| `add_audio`                   | Add a track to your library                  |
| `delete_audio`                | Delete a track from your library             |
| `edit_audio`                  | Edit track artist and title                  |
| `reorder_audio`               | Change track order in library                |
| `get_popular_audios`          | Get globally popular tracks                  |
| `get_suggested_audios`        | Get recommended tracks for a user            |
| `search_audio`                | Search tracks by query                       |
| `search_albums`               | Search albums by query                       |
| `search_artists`              | Search artists by query                      |
| `search_playlists`            | Search playlists by query                    |
| `get_artist_by_id`            | Get artist profile                           |
| `get_albums_by_artist`        | Get albums by an artist                      |
| `get_audios_by_artist`        | Get tracks by an artist                      |
| `get_playlists`               | Get playlists for an owner                   |
| `get_playlist_by_id`          | Get a specific playlist                      |
| `create_playlist`             | Create a new playlist                        |
| `delete_playlist`             | Delete a playlist                            |
| `follow_playlist`             | Follow/save a playlist                       |
| `add_audio_to_playlist`       | Add tracks to a playlist                     |
| `remove_audios_from_playlist` | Remove tracks from a playlist                |

---
