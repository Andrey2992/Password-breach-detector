# Importas la clase desde su ubicación
from src.models.password_entry import PasswordEntry
from src.services.pwned_api import check_password_prefix, get_password_leaks_count

# Creas un objeto de prueba
entrada = PasswordEntry("contraseña123")  # Puedes cambiar la contraseña para probar con otras
# Imprimes sus valores para verificar
print("Password:", entrada.password)
print("Hash:", entrada.hash_sha1)
print("Breach Count (por defecto):", entrada.breach_count)

# 1. Traemos la respuesta de la API
resultado = check_password_prefix(entrada.hash_sha1[:5])  # Usamos los primeros 5 caracteres del hash SHA-1

# 2. Buscamos nuestro sufijo en esa respuesta
conteo = get_password_leaks_count(resultado, entrada.hash_sha1[5:])  # Usamos el sufijo del hash SHA-1

# 3. Imprimimos el resultado final
print("Número de filtraciones encontradas:", conteo)