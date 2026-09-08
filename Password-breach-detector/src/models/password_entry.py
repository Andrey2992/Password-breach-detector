
#basicamente e creo esta clase para almacenar la información de una contraseña, su hash SHA-1 
# y la cantidad de veces que ha sido comprometida en violaciones de seguridad.
import hashlib
from itertools import count


class PasswordEntry: 
        def __init__(self, password: str):
            self.password = password
        # Calculamos el hash automáticamente a partir de la contraseña
            self.hash_sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
            self.breach_count = 0

        def set_breach_count(self, count: int) -> None:
            self.breach_count = count