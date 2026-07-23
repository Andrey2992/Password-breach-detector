
#basicamente e creo esta clase para almacenar la información de una contraseña, su hash SHA-1 
# y la cantidad de veces que ha sido comprometida en violaciones de seguridad.
class PasswordEntry: 
    def __init__(self,password: str,hash_sha1: str,breach_count: int = 0 ): #se creo el metodo constructor __init__ que inicializa
        #con tres atributos: password, hash_sha1 y breach_count.
        self.password = password  #password es un atributo que almacena la contraseña en texto plano.
        self.hash_sha1 = hash_sha1 #hash_sha1 es un atributo que almacena el hash SHA-1 de la contraseña, que es una representación segura de la contraseña.
        self.breach_count = breach_count #breach_count es un atributo que almacena la cantidad de veces que la contraseña
                                        #ha sido comprometida en violaciones de seguridad y el int = 0 significa que por defecto se inicializa en cero
                                        #es decir, si no se proporciona un valor para breach_count al crear una instancia de PasswordEntry, 
                                        # se asumirá que la contraseña no ha sido comprometida.

