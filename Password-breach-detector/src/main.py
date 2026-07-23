import hashlib

def generar_hash(password): #es str <(string)
    
    """Basicamnete convierte un texto plano en su equivalente Hash SHA-1 en mayúsculas."""
    # Convertimos el string a bytes codificados en UTF-8 y luego aplicamos SHA-1
    resultado_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper() #como funciona? bueno, primero se codifica la contraseña 
                                                      #en bytes usando UTF-8, luego se calcula el hash SHA-1 de esos bytes y finalmente se convierte
                                                      #a una cadena hexadecimal en mayúsculas.
    return resultado_hash

# --- BLOQUE DE PRUEBA LOCAL ---
if __name__ == "__main__": #este sirve para que el bloque de prueba solo se ejecute 
                        # si este archivo es el principal que se está ejecutando, y no cuando se importa como módulo en otro archivo.
    password_prueba = "password123"
    hash_completo = generar_hash(password_prueba) # aqui generamos el hash completo de la contraseña de prueba
    
    # Aplicamos k-Anonymity: cortamos el hash en 2 partes
    prefijo_5 = hash_completo[:5]
    resto_hash = hash_completo[5:]
    
    print("=" * 50)
    print(f"Contraseña original: {password_prueba}")
    print(f"Hash completo (SHA-1): {hash_completo}")
    print("-" * 50)
    print(f"1. Lo que ENVIAMOS a la API (primeros 5): {prefijo_5}")
    print(f"2. Lo que GUARDAMOS en secreto (resto):  {resto_hash}")
    print("=" * 50)