# Actividad 3: Uso de interfaces y métodos - decorator.py

"""En el código siguiente, a partir de la interfaz Componente base y ObjetoConcreto,
declara una interfaz formal para un Patrón Decorator Base e declara dos decoradores: SoporteGmail y SoporteFacebook.
Utiliza como referencia los ejemplos de Decorator presentados en clase al revisar el tema de Patrones de Diseño.
Recuerda que en este patrón, los decoradores tienen un método, 
en el cual mandan a llamar el método correspondiente al objeto concreto (en este caso, la clase Autenticacion),
pero le dan un manejo único, distinto al objeto concreto."""

from abc import ABC, abstractmethod

# Interfaz Componente base
class Auth(ABC):
    @abstractmethod
    def iniciarSesion(self, usuario, password):
        pass

# ObjetoConcreto que implementa la interfaz base
class Autenticacion(Auth):
    def iniciarSesion(self, usuario, password):
        print(f"Iniciando sesión con el usuario: {usuario} desde el autenticador base")

# Decorador base que también implementa la interfaz Componente
class DecoradorAuth(Auth):
    def __init__(self, auth: Auth):
        self._auth = auth

    def iniciarSesion(self, usuario, password):
        self._auth.iniciarSesion(usuario, password)

# Decorador SoporteGmail
class SoporteGmail(DecoradorAuth):
    def iniciarSesion(self, usuario, password):
        print("[Gmail] Validando credenciales en Gmail...")
        super().iniciarSesion(usuario, password)
        print("[Gmail] Sesión iniciada exitosamente en Gmail.")

# Decorador SoporteFacebook
class SoporteFacebook(DecoradorAuth):
    def iniciarSesion(self, usuario, password):
        print("[Facebook] Validando credenciales en Facebook...")
        super().iniciarSesion(usuario, password)
        print("[Facebook] Sesión iniciada exitosamente en Facebook.")

# Ejemplo de uso
autenticador = Autenticacion()

authgmail = SoporteGmail(autenticador)
authgmail.iniciarSesion("usuario1@gmail.com", "pass789")

authfacebook = SoporteFacebook(autenticador)
authfacebook.iniciarSesion("nombredeusuario123", "pass456")

# Comentarios:
# - Se implementó una interfaz formal para el Decorador Base, `DecoradorAuth`, que extiende la funcionalidad del componente base.
# - Los decoradores `SoporteGmail` y `SoporteFacebook` agregan comportamientos específicos antes y después de llamar al método `iniciarSesion` del objeto decorado.
# - Este diseño permite extender la funcionalidad de `Autenticacion` sin modificar su código, respetando el principio de abierto/cerrado (OCP).
