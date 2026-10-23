from src.view.song_register_view import SongRegisterView

def song_register_process():
    song_register_view = SongRegisterView()
    
    new_song_information = song_register_view.registry_song_initial()
    # Enviar new_song_informations para controller