class SongRegisterController:
    def insert(self, new_song_informations: dict) -> dict:
        verify_songs_info()
        self.__verify_if_song_already_registered()
        verify_if_song_already_registered()
        insert_song()
        format_response()
        pass
    
    def __verify_if_song_already_registered(new_song_informations: dict) -> None:
        pass
    
    def verify_songs_info(new_song_informations: dict) -> None:
        pass
    
    def insert_song() -> None:
        pass
    
    def format_response() -> None:
        pass