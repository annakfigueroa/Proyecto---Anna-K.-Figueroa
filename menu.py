import json
import uuid 
from user import Listener, Musician, User
from music import Tracklist, Playlist, Album

class Menu: 
    def __init__(self):
        self.users = []
        self.listeners = []
        self.musicians = []
        self.load_users()
   
        #Carga los datos del usuario de los archivos de tipo json,
        #los convierte en objetos al agregarlo a la lista que forma parte de los
        #atributos homónimos 
    def load_users(self):
        with open("Proyecto\\users.json","r",encoding="UTF-8") as data:
            cargar_users = json.load(data)
            for user in cargar_users:
                if user["type"] =="listener":
                    listeners = User(user["id"], user["name"],user["email"], user["username"], user["type"])
                    self.users.append(listeners)
                else:
                    musicians = User(user["id"], user["name"],user["email"], user["username"], user["type"])
                    self.users.append(musicians)
        return self.users

    #Función para crear un usuario nuevo
    def create_users(self):
        nombre = input ("Ingresa tu nombre: ")
        email = input ("Ingresa tu correo Gmail o UNIMET: ")
        #Validación 1 para el E-mail
        if "@" not in email:
            print(">>Direccion de correo invalida")
            email = input ("Ingresa tu email: ")
        #Validación 2 para el E-mail
        elif not email.endswith(".edu.ve") or not email.endswith("gmail.com"):
            print(">>Direccion de correo invalida")
            email = input ("Ingresa tu email: ")
        tipo = input ("Indica tu tipo de usuario -listener/musician: ")
        #Validación para el tipo de usuario   
        if "listener" or "musician" not in tipo:
            print (">>Tipo de usuario invalido")
            tipo = input ("Indica tu tipo de usuario -->listener/musician: ")
        rand_id = uuid.uuid1
        namespace=uuid.NAMESPACE_URL
        nombre_id = nombre
        #Se asigna un id específico a cada usuario 
        uuidfromn = uuid.uuid5(namespace,nombre_id)
        id=uuidfromn
        #Se asigna un username específico a cada usuario 
        username = rand_id
        usuario= User(id=id, name=nombre, email=email, type=tipo, username=username)
        self.users.append(usuario)
        
    #Función para guardar los datos de los usuarios en un archivo .txt y crear la database
    def save_users(self):
        with open("users.txt", "w") as file:
            for usuario in self.users:
                file.write(usuario)
    
    #Función para buscar un usuario por su nombre
    def search_users(self,nombre):
        #Busca un usuario por su nombre
        nombre = input("Escribe el nombre: ")
        for usuario in self.users:
            if nombre == usuario.get_name():
                return usuario
    
    #Función para actualizar los datos de un usuario mediante input
    def update_users(self):
        nombre = input('Ingrese el nombre del usuario a actualizar: ')
        usuario = next((user for user in self.users if user.get_name() == nombre), None)
        if usuario:
            usuario.set_name(input('Ingrese el nuevo nombre: '))
            usuario.set_email(input('Ingrese el nuevo correo: '))
            usuario.set_username(input('Ingrese el nuevo nombre de usuario: '))
            usuario.set_type(input('Ingrese el nuevo tipo de usuario (listener/musician): '))
            self.users = [for user in self.users if u.name == nombre else u for u in self.users] 
            with open('users.txt', 'w') as file:
                for user in self.users:
                    file.write(str(user) + '\n')
        else:
            print('No se encontró ningún usuario con ese nombre.')
    
    #Función para borrar un usuario
    def delete_user_by_input(self):
        user_id_or_name = input("Introduce tu nombre o ID: ")
        user_to_delete = None
        for user in self.users:
            if user_id_or_name == user.id or user_id_or_name == user.name:
                user_to_delete = user
                break
        if user_to_delete:
            self.users.remove(user_to_delete)
        else:
            print("No se encuentra un usuario con este nombre o ID.")
    
    #Función para ver los perfiles de otras personas
    def view_users(self):
        n_u = input("¿Qué usuario deseas buscar? Introduce el nombre: ")
        t_u = input ("Introduce el tipo de usuario (listener/musician): ")
        for i in t_u:
            for i in range(len(self.users)):
                print (f"Nombre: {self.users.type}")
            if ["type"] == "listener":
                for name in range(len(self.users)):
                    if n_u == self.listeners.type
                        print (f"Usuario: {self.listeners.liked_albums}, Canciones gustadas: {self.listeners.liked_songs}, 
                               Álbumes gustados: {self.listeners.liked_albums},")
            elif ["type"] == "musician":
                for name in range(len(self.users)):
                    if n_u == self.listeners.type:
                        print (Musician(id=[], name =[], email = [], username = [], type= [], albums=self.albums, streams= int = 0))
                        print (f"Streams: {self.streams}")
                        

    #Función para correr el programa
    def test(self):
        while True:
            print(">>BIENVENIDO A METROTIFY>>")
            menu=int(input("""
            Elige una opción:
            1. Gestión de perfil
            2. Gestión de música
            3. Gestión de interacciones
            4. Stats
            5. Salir
            >>> """))
            if menu == 1:
                menu1=int(input("""
                Escoge una de las siguientes opciones:
                1. Registrar un usuario nuevo
                2. Buscar un perfil
                3. Cambiar la info de la cuenta
                4. Borrar los datos de la cuenta
                5. Ver los perfiles de otros usuarios
                >>> """))
                if menu1 == 1:
                    self.create_users()
                    break
                elif menu1 == 2:      
                    self.search_users(self)
                elif menu1== 3:
                    self.update_users()
                elif menu1==4:
                    self.delete_user_by_input()
                elif menu1 == 5:
                    self.view_users()
            elif menu == 5:
                self.load_users()
                self.save_users()
                print ("Hasta la proxima!")
                exit()
            else:
                print("Opción inválida. Intenta de nuevo.")                       
Menu()
