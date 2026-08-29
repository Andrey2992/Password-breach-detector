# Importas la clase desde su ubicación
from src.models.password_entry import PasswordEntry
from src.services.pwned_api import check_password_prefix, get_password_leaks_count

# Creas un objeto de prueba
entrada = PasswordEntry("mi_contraseña_secreta", "5BAA61E4C9B93F3F0682250B6CF8331B7EE68FD8")

# Imprimes sus valores para verificar
print("Password:", entrada.password)
print("Hash:", entrada.hash_sha1)
print("Breach Count (por defecto):", entrada.breach_count)

# 1. Traemos la respuesta de la API
resultado = check_password_prefix("5BAA6")

# 2. Buscamos nuestro sufijo en esa respuesta
conteo = get_password_leaks_count(resultado, "1E4C9B93F3F0682250B6CF8331B7EE68FD8")

# 3. Imprimimos el resultado final
print("Número de filtraciones encontradas:", conteo)