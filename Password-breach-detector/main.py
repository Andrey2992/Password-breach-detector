# Importas la clase desde su ubicación
from src.models.password_entry import PasswordEntry

# Creas un objeto de prueba
entrada = PasswordEntry("mi_contraseña_secreta", "5BAA61E4C9B93F3F0682250B6CF8331B7EE68FD8")

# Imprimes sus valores para verificar
print("Password:", entrada.password)
print("Hash:", entrada.hash_sha1)
print("Breach Count (por defecto):", entrada.breach_count)