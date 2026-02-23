from requests import Session

class VkAudio:
    def __init__(
            self,
            access_token: str,
            api_version: str = "5.122") -> None:
        self.api = "https://api.vk.com/method"
        self.api_version = api_version
        self.access_token = access_token
        self.session = Session()
        self.session.headers = {
            "User-Agent": "VKAndroidApp/6.2-5091 (Android 9; SDK 28; samsungexynos7870; samsung j6lte; 720x1450)"
        }

    def get_audio(self, owner_id: int, count: int = 100) -> dict:
        return self.session.get(
            f"{self.api}/audio.get?access_token={self.access_token}&owner_id={owner_id}&count={count}&v={self.api_version}").json()

    def add_audio(self, owner_id: int, audio_id: int) -> dict:
        return self.session.get(
            f"{self.api}/audio.add?access_token={self.access_token}&owner_id={owner_id}&audio_id={audio_id}&v={self.api_version}").json()

    def add_audio_to_playlist(
            self,
            owner_id: int,
            playlist_id: int,
            audio_ids: str) -> dict:
        return self.session.get(
            f"{self.api}/audio.addToPlaylist?access_token={self.access_token}&owner_id={owner_id}&playlist_id={playlist_id}&audio_ids={audio_ids}&v={self.api_version}").json()
    
    def create_playlist(
            self,
            owner_id: int,
            title: str) -> dict:
        return self.session.get(
            f"{self.api}/audio.createPlaylist?access_token={self.access_token}&owner_id={owner_id}&title={title}&v={self.api_version}").json()

    def delete_playlist(
            self,
            owner_id: int,
            playlist_id: int) -> dict:
        return self.session.get(
            f"{self.api}/audio.deletePlaylist?access_token={self.access_token}&owner_id={owner_id}&playlist_id={playlist_id}&v={self.api_version}").json()

    def follow_playlist(
            self,
            owner_id: int,
            playlist_id: int) -> dict:
        return self.session.get(
            f"{self.api}/audio.followPlaylist?access_token={self.access_token}&owner_id={owner_id}&playlist_id={playlist_id}&v={self.api_version}").json()

    def remove_audios_from_playlist(
            self,
            owner_id: int,
            playlist_id: int,
            audio_ids: str) -> dict:
            return self.session.get(
                f"{self.api}/audio.removeFromPlaylist?access_token={self.access_token}&owner_id={owner_id}&playlist_id={playlist_id}&audio_ids={audio_ids}&v={self.api_version}").json()

    def delete_audio(
            self,
            owner_id: int,
            audio_id: int) -> dict:
        return self.session.get(
            f"{self.api}/audio.delete?access_token={self.access_token}&owner_id={owner_id}&audio_id={audio_id}&v={self.api_version}").json()

    def edit_audio(
            self,
            owner_id: int,
            audio_id: int,
            artist: str,
            title: str) -> dict:
        return self.session.get(
            f"{self.api}/audio.edit?access_token={self.access_token}&owner_id={owner_id}&audio_id={audio_id}&artist={artist}&title={title}&v={self.api_version}").json()
    
    def search_audio(
            self,
            query: str,
            count: int = 10) -> dict:
        return self.session.get(
                f"{self.api}/audio.search?access_token={self.access_token}&q={query}&count={count}&v={self.api_version}").json()
    
    def reorder_audio(
            self,
            owner_id: int,
            audio_id: int,
            before_audio_id: int) -> dict:
        return self.session.get(
            f"{self.api}/audio.reorder?access_token={self.access_token}&owner_id={owner_id}&audio_id={audio_id}&before={before_audio_id}&v={self.api_version}").json()
    
    def search_albums(
            self,
            query: str,
            count: int = 10) -> dict:
        return self.session.get(
            f"{self.api}/audio.searchAlbums?access_token={self.access_token}&q={query}&count={count}&v={self.api_version}").json()
    
    def search_artists(
            self,
            query: str,
            count: int = 10) -> dict:
        return self.session.get(
            f"{self.api}/audio.searchArtists?access_token={self.access_token}&q={query}&count={count}&v={self.api_version}").json()
    
    def search_playlists(
            self,
            query: str,
            count: int = 10,
            filters: str = "albums") -> dict:
        return self.session.get(
            f"{self.api}/audio.searchPlaylists?access_token={self.access_token}&q={query}&count={count}&filters={filters}&v={self.api_version}").json()
    
    def get_popular_audios(self, count: int = 10) -> dict:
        return self.session.get(
            f"{self.api}/audio.getPopular?access_token={self.access_token}&count={count}&v={self.api_version}").json()
    
    def get_suggested_audios(
            self,
            target_id: str,
            count: int = 10,
            offset: int = 20) -> dict:
        return self.session.get(
            f"{self.api}/audio.getRecommendations?access_token={self.access_token}&target_id={target_id}&count={count}&offset={offset}&v={self.api_version}").json()
    
    def get_albums_by_artist(
            self,
            artist_id: int,
            count: int = 10) -> dict:
        return self.session.get(
            f"{self.api}/audio.getAlbumsByArtist?access_token={self.access_token}&artist_id={artist_id}&count={count}&v={self.api_version}").json()
    
    def get_artist_by_id(
            self,
            artist_id: int,
            extended: int = 1) -> dict:
        return self.session.get(
            f"{self.api}/audio.getArtistById?access_token={self.access_token}&artist_id={artist_id}&extended={extended}&v={self.api_version}").json()
    
    def get_audios_by_artist(
            self,
            artist_id: int,
            count: int = 10) -> dict:
        return self.session.get(
            f"{self.api}/audio.getAudiosByArtist?access_token={self.access_token}&artist_id={artist_id}&count={count}&v={self.api_version}").json()
        
    def get_audio_by_id(self, audio_ids: str) -> dict:
        return self.session.get(
            f"{self.api}/audio.getById?access_token={self.access_token}&audios={audio_ids}&v={self.api_version}").json()
        
    def get_audios_count(self, owner_id: int) -> dict:
            return self.session.get(
                f"{self.api}/audio.getCount?access_token={self.access_token}&owner_id={owner_id}&v={self.api_version}").json()
        
    def get_lyrics_for_audio(self, lyrics_id: int) -> dict:
            return self.session.get(
                f"{self.api}/audio.getLyrics?access_token={self.access_token}&lyrics_id={lyrics_id}&v={self.api_version}").json()
        
    def get_playlist_by_id(
            self,
            owner_id: int,
            playlist_id: int,
            access_key: int,
            count: int = 10) -> dict:
        return self.session.get(
            f"{self.api}/audio.getPlaylistById?access_token={self.access_token}&owner_id={owner_id}&playlist_id={playlist_id}&access_key={access_key}&count={count}&v={self.api_version}").json()
        
    def get_playlists(
            self,
            owner_id: int,
            count: int = 10) -> dict:
        return self.session.get(
            f"{self.api}/audio.getPlaylists?access_token={self.access_token}&owner_id={owner_id}&count={count}&v={self.api_version}").json()
