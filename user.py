#Se define la clase Padre Usuario
class User(object):
    def __init__(self, id, name, email, username, type):
        self.id = id
        self.name = name
        self.email = email 
        self.username = username
        self.type = type
    def view(self):
        return (self.id, self.name, self.email, self.username, self.type)
    
#Se define la clase Oyente
class Listener(User):
    def __init__(self, id, name, email, username, type, liked_albums=[], liked_playlists=[], liked_songs=[], playlists=[]):
        super().__init__(id, name, email, username, type)
        self.liked_albums = liked_albums
        self.liked_playlists = liked_playlists
        self.liked_songs = liked_songs
        self.playlists = playlists
        
#Se define la clase Músico
class Musician(User):
    def __init__(self, id, name, email, username, type, albums=[], streams=0):
        super().__init__(id, name, email, username, type)
        self.albums = albums
        self.streams = streams 


