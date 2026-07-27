import requests #esta librería se utiliza para realizar solicitudes HTTP, 
#lo que permite interactuar con la API de Have I Been Pwned para verificar si una contraseña
# ha sido comprometida en violaciones de seguridad.

#QUE ES UN SOLICITUD HTTP? es una petición que un cliente (como un navegador web o una aplicación) hace a un servidor para solicitar información o realizar una acción.
#QUE ES UNA API? son protocolosque permiten que diferentes aplicaciones se comuniquen entre sí, facilitando el intercambio de datos y funcionalidades.

PWNED_API_URL = "https://api.pwnedpasswords.com/range/" #esta constante almacena la URL base de la API de Have I Been Pwned,
# que se utiliza para verificar si una contraseña ha sido comprometida en violaciones de seguridad.

#digamos esta clase que hace? 
#para que sirve? basicamente esta clase se encarga de interactuar con la API de Have I Been Pwned para verificar si una contraseña ha sido comprometida en violaciones de seguridad.
def check_password_prefix(prefix: str):
    url = PWNED_API_URL + prefix #esta línea construye la URL 
    #completa para la solicitud a la API,
    
    
    #para que sirve import requests? b
    #basicamente esta libreria se utiliza para realizar solicitudes HTTP,
    # lo que permite interactuar con la API de Have I Been Pwned para verificar si una contraseña ha sido comprometida en violaciones de seguridad.
    #2- Peticion HTTP 
    response= requests.get(url) #esta línea realiza una solicitud HTTP GET a la URL construida anteriormente,
    # que envía el prefijo de la contraseña a la API
    
    #3- Ahora, se hizo esta condicional para ver si la solicitud fue buena
    if response.status_code != 200:
        raise RuntimeError(f"Error fetching data from Pwned API: {response.status_code}") #si la solicitud no fue exitosa, se lanza un error con un mensaje que indica el código de estado de la respuesta.
    return response.text #si fue buena la solicitud se almacena aca