from user import Listener, Musician, User
#Se define la Clase Padre para las hijas Album y Playlist
class Music():
    def __init__(self,id, name):
        self.id = id
        self.name = name
        
#Se define la Clase Tracklist
class Tracklist(Music):
    def __init__(self, id, name, duration, link):
        super().__init__(id, name)
        self.duration = duration
        self.link = link

#Se define la clase Playlist
class Playlist(Music):
    def __init__(self, id, name, description, creator,track):
        super().__init__(id, name)
        self.description=description
        self.creator=creator
        #Se llama al atributo id de la clase Tracklist porque es 
        #una lista de tracks que están presentes en el Tracklist
        self.track = [track.id]
        
#Se define la clase Album
class Album(Music):
    def __init__(self, id, name, description, cover, published, genre, artist, tracklist):
        super().__init__(id, name)
        self.description = description
        self.cover = cover
        self.published = published
        self.genre = genre
        self.artist = [artist.id]
        self.tracklist = Tracklist
        
        