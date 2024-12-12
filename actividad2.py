## Actividad 2: Principios SOLID aplicados - habitacion_hotel.py

"""En esta actividad, se presenta un problema que ya hemos resuelto en clase en un parcial anterior.
Sin embargo, la implementación actual no es la más eficiente y ha resultado ser compleja y redundante,
especialmente al acceder a los costos de los diferentes servicios debido a la dependencia de objetos concretos sin el uso adecuado de abstracciones.
Tu tarea consiste en modificar el código existente utilizando un patrón de diseño y aplicando un principio SOLID,
con el objetivo de mejorar su legibilidad y eficiencia.
Al finalizar, incluye comentarios en el código que expliquen qué patrón o principio SOLID has aplicado, 
los cambios principales que realizaste y cómo funciona ahora tu implementación."""

from abc import ABC, abstractmethod

# Aplicamos el principio de responsabilidad única (SRP) y el patrón de diseño Composición.
class Habitacion:
    def __init__(self, numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad

    def reservar(self):
        print(f"Habitación {self.numero} con capacidad para {self.capacidad} personas reservada.")

# Clase abstracta para servicios adicionales, siguiendo el principio de sustitución de Liskov (LSP).
class ServicioAdicional(ABC):
    def __init__(self, nombre, costo):
        self.nombre = nombre
        self.costo = costo

    @abstractmethod
    def ofrecer(self):
        pass

class Restaurante(ServicioAdicional):
    def ofrecer(self):
        print(f"Restaurante '{self.nombre}', costo adicional: ${self.costo} por persona.")

class Spa(ServicioAdicional):
    def ofrecer(self):
        print(f"Spa '{self.nombre}', costo adicional: ${self.costo} por día.")

# La clase Hotel ahora usa composición en lugar de herencia múltiple para respetar el principio de segregación de interfaces (ISP).
class Hotel:
    def __init__(self, nombre_hotel, habitacion, servicios):
        self.nombre_hotel = nombre_hotel
        self.habitacion = habitacion
        self.servicios = servicios

    def generar_reserva(self):
        print(f"Generando reserva en el hotel '{self.nombre_hotel}'")
        self.habitacion.reservar()
        for servicio in self.servicios:
            servicio.ofrecer()

# Ejemplo de uso
habitacion = Habitacion(13, 3)
restaurante = Restaurante("Sirenita", 100)
spa = Spa("Don Chuy", 50)

hotel_california = Hotel("Hotel California", habitacion, [restaurante, spa])
hotel_california.generar_reserva()

# Comentarios:
# - Se aplicó el principio de responsabilidad única (SRP): cada clase tiene una única responsabilidad.
# - Se eliminó la herencia múltiple y se utilizó composición, lo que mejora la legibilidad y respeta el principio de segregación de interfaces (ISP).
# - Se introdujo la clase abstracta ServicioAdicional para que los servicios adicionales implementen su lógica específica, siguiendo el patrón de diseño de abstracción.
# - La clase Hotel no necesita conocer los detalles de implementación de los servicios, respetando el principio de inversión de dependencias (DIP).
