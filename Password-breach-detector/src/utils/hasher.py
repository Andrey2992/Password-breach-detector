import hashlib # se importa la biblioteca hashlib, 
# que proporciona funciones de hash criptográficas, incluyendo SHA-1.
#ejemplo de uso:  un ejmplo de uso de esta función podría ser generar_hash_sha1("mi_contraseña") para obtener el hash SHA-1 de la contraseña "mi_contraseña".

def generar_hash_sha1(password): #realizamos una funcion que recibe un parámetro llamado password, 
    """
    Convierte el texto plano en su equivalente Hash SHA-1 en mayúsculas.
    
    Args:
        password (str): La contraseña en texto plano. 

    Returns:
        str: El hash SHA-1 de la contraseña en mayúsculas. 
    """
    password_bytes = password.encode('utf-8') # creamos una variable que almacena la contraseña
    # basicamente convierte la contraseña de texto plano en bytes codificados en UTF-8, ya que se debe trabajar en bytes para calcular el hash.
    hash_objeto = hashlib.sha1(password_bytes) #aqui se calcula el hash SHA-1 de esos bytes utilizando la función sha1() de hashlib, que devuelve un objeto de hash.
    hash_hex = hash_objeto.hexdigest().upper() #este objeto de hash se convierte en una cadena hexadecimal utilizando hexdigest(), y luego se convierte a mayúsculas con upper().
    
    return hash_hex # finalmente, la función devuelve el hash SHA-1 en mayúsculas como una cadena de texto.


#Resume: In english
#Well, what we understand from this code? basically, this code define a function called generar_hash_sha1 that take a password and makes a from text plain to bytes
# and then generates a calculate SHA-1the SHA-1 hash of that password in uppercase. 
# It also includes a docstring that explains the function's purpose, its arguments, and its return value. The code uses the hashlib library to perform the hashing operation.

#Resumen en español xd: lo que hace es pasar la contraseña digamos de texto plano a bytes y ya una ves se hace el calculo se devuelve a cadena de texto con hexadecimales

