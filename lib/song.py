class Song:

    artists = []
    genres = []
    count = 0
    genre_count = {}
    artist_count= {}

    def __init__(self, nombre, artista, janra):

        self.name = nombre
        self.artist = artista
        self.genre = janra
        self.song_counter()
        self.artist_array(artista)
        self.genre_array(janra)
        self.add_to_genre_count(janra)
        self.add_to_artist_count(artista)

    @classmethod
    def song_counter(cls, increment = 1):
        cls.count += increment
    
    @classmethod
    def artist_array(cls, artist):
        cls.artists.append(artist)
    
    @classmethod
    def genre_array(cls, janra):
        cls.genres.append(janra)
    
    @classmethod
    def add_to_genre_count(cls, janra):
        if janra in cls.genre_count:
            cls.genre_count[janra] += 1
        else:
            cls.genre_count[janra] = 1
    @classmethod
    def add_to_artist_count(cls, artista):
        if artista in cls.artist_count:
            cls.artist_count[artista] += 1
        else:
            cls.artist_count[artista] = 1
   


