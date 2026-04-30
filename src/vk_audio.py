from requests import Session

class VkAudio:
    def __init__(
            self,
            access_token: str,
            api_version: str = "5.199") -> None:
        self.api = "https://api.vk.com/method"
        self.api_version = api_version
        self.access_token = access_token
        self.session = Session()
        self.session.headers = {
            "User-Agent": "VKAndroidApp/6.2-5091 (Android 9; SDK 28; samsungexynos7870; samsung j6lte; 720x1450)"
        }

    def _get(self, method: str, params: dict = None) -> dict:
        payload = {
            "access_token": self.access_token,
            "v": self.api_version
        }
        if params:
            payload.update(params)
        return self.session.get(
            f"{self.api}/{method}", params=payload).json()

    def get_audio(self, owner_id: int, count: int = 100) -> dict:
        params = {
            "owner_id": owner_id,
            "count": count
        }
        return self._get("audio.get", params)

    def add_audio(self, owner_id: int, audio_id: int) -> dict:
        params = {
            "owner_id": owner_id,
            "audio_id": audio_id
        }
        return self._get("audio.add", params)

    def add_audio_to_playlist(
            self,
            owner_id: int,
            playlist_id: int,
            audio_ids: str) -> dict:
        params = {
            "owner_id": owner_id,
            "playlist_id": playlist_id,
            "audio_ids": audio_ids
        }
        return self._get("audio.addToPlaylist", params)

    def create_playlist(self, owner_id: int, title: str) -> dict:
        params = {
            "owner_id": owner_id,
            "title": title
        }
        return self._get("audio.createPlaylist", params)

    def delete_playlist(self, owner_id: int, playlist_id: int) -> dict:
        params = {
            "owner_id": owner_id,
            "playlist_id": playlist_id
        }
        return self._get("audio.deletePlaylist", params)

    def follow_playlist(self, owner_id: int, playlist_id: int) -> dict:
        params = {
            "owner_id": owner_id,
            "playlist_id": playlist_id
        }
        return self._get("audio.followPlaylist", params)

    def remove_audios_from_playlist(
            self,
            owner_id: int,
            playlist_id: int,
            audio_ids: str) -> dict:
        params = {
            "owner_id": owner_id,
            "playlist_id": playlist_id,
            "audio_ids": audio_ids
        }
        return self._get("audio.removeFromPlaylist", params)

    def delete_audio(self, owner_id: int, audio_id: int) -> dict:
        params = {
            "owner_id": owner_id,
            "audio_id": audio_id
        }
        return self._get("audio.delete", params)

    def edit_audio(
            self,
            owner_id: int,
            audio_id: int,
            artist: str,
            title: str) -> dict:
        params = {
            "owner_id": owner_id,
            "audio_id": audio_id,
            "artist": artist,
            "title": title
        }
        return self._get("audio.edit", params)

    def search_audio(self, query: str, count: int = 10) -> dict:
        params = {
            "q": query,
            "count": count
        }
        return self._get("audio.search", params)

    def reorder_audio(
            self,
            owner_id: int,
            audio_id: int,
            before_audio_id: int) -> dict:
        params = {
            "owner_id": owner_id,
            "audio_id": audio_id,
            "before": before_audio_id
        }
        return self._get("audio.reorder", params)

    def search_albums(self, query: str, count: int = 10) -> dict:
        params = {
            "q": query,
            "count": count
        }
        return self._get("audio.searchAlbums", params)

    def search_artists(self, query: str, count: int = 10) -> dict:
        params = {
            "q": query,
            "count": count
        }
        return self._get("audio.searchArtists", params)

    def search_playlists(
            self,
            query: str,
            count: int = 10,
            filters: str = "albums") -> dict:
        params = {
            "q": query,
            "count": count,
            "filters": filters
        }
        return self._get("audio.searchPlaylists", params)

    def get_popular_audios(self, count: int = 10) -> dict:
        params = {
            "count": count
        }
        return self._get("audio.getPopular", params)

    def get_suggested_audios(
            self,
            target_id: str,
            count: int = 10,
            offset: int = 20) -> dict:
        params = {
            "target_id": target_id,
            "count": count,
            "offset": offset
        }
        return self._get("audio.getRecommendations", params)

    def get_albums_by_artist(
            self, artist_id: int, count: int = 10) -> dict:
        params = {
            "artist_id": artist_id,
            "count": count
        }
        return self._get("audio.getAlbumsByArtist", params)

    def get_artist_by_id(
            self, artist_id: int, extended: int = 1) -> dict:
        params = {
            "artist_id": artist_id,
            "extended": extended
        }
        return self._get("audio.getArtistById", params)

    def get_audios_by_artist(
            self, artist_id: int, count: int = 10) -> dict:
        params = {
            "artist_id": artist_id,
            "count": count
        }
        return self._get("audio.getAudiosByArtist", params)

    def get_audio_by_id(self, audio_ids: str) -> dict:
        params = {
            "audios": audio_ids
        }
        return self._get("audio.getById", params)

    def get_audios_count(self, owner_id: int) -> dict:
        params = {
            "owner_id": owner_id
        }
        return self._get("audio.getCount", params)

    def get_lyrics_for_audio(self, lyrics_id: int) -> dict:
        params = {
            "lyrics_id": lyrics_id
        }
        return self._get("audio.getLyrics", params)

    def get_playlist_by_id(
            self,
            owner_id: int,
            playlist_id: int,
            access_key: int,
            count: int = 10) -> dict:
        params = {
            "owner_id": owner_id,
            "playlist_id": playlist_id,
            "access_key": access_key,
            "count": count
        }
        return self._get("audio.getPlaylistById", params)

    def get_playlists(self, owner_id: int, count: int = 10) -> dict:
        params = {
            "owner_id": owner_id,
            "count": count
        }
        return self._get("audio.getPlaylists", params)
