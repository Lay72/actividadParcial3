# Actividad 4: Ejercicio Bonificaciones tipos_metodos.py
"""En una empresa, se desea implementar un sistema orientado a objetos para calcular las bonificaciones que reciben los empleados al final del mes. Este cálculo considera dos tipos de bonificaciones:

* Bonificación por antigüedad: Está relacionada con el número de años trabajados en la empresa.
* Bonificación general: Es un monto fijo que se aplica a todos los empleados de la empresa y no depende de la antigüedad.

Se te pide implementar un programa orientado a objetos que contenga los siguientes elementos:
Atributos privados: 
* Nombre del empleado
* Antigüedad en años
* Salario base mensual

Atributo estático
* Bonificación general fija de #300 
Métodos:
* calcular bonificación general, que devuelve el valor de la bonificación fija (método de clase)
* calcular bonificación según su antigüedad, utilizando la fórmula:
bonificación de antiguedad = antigüedad x100 (método de instancia)
* Calcular bonificación total: retorna la suma de la bonificación general y bonificación por antiguedad, ya sea que esté almacenada en l instancia, o calcularla dinámicamente. 

Implementa los tipos de métodos que se indiquen y por cada atributo privado crea su getter y su setter utilizando métodos de property. 
Para el caso de uso, contempla lo siguiente:
* Crear una instancia de la clase para un empleado de ejemplo.
* Mostrar el nombre del empleado, su antigüedad, y su salario base.
* Calcular y mostrar la bonificación general (utilizando el método estático sin ninguna instancia) y almacenar el resultado
* Calcular y mostrar la bonificación por antigüedad del empleado.
* Calcular y mostrar la bonificación total (suma de la general y la de antigüedad)."""

class Empleado:
    BONIFICACION_GENERAL = 300

    def __init__(self, nombre, antiguedad, salario_base):
        self._nombre = nombre
        self._antiguedad = antiguedad
        self._salario_base = salario_base

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def antiguedad(self):
        return self._antiguedad

    @antiguedad.setter
    def antiguedad(self, valor):
        self._antiguedad = valor

    @property
    def salario_base(self):
        return self._salario_base

    @salario_base.setter
    def salario_base(self, valor):
        self._salario_base = valor

    @classmethod
    def calcular_bonificacion_general(cls):
        return cls.BONIFICACION_GENERAL

    def calcular_bonificacion_antiguedad(self):
        return self._antiguedad * 100

    def calcular_bonificacion_total(self):
        return self.calcular_bonificacion_general() + self.calcular_bonificacion_antiguedad()

empleado = Empleado("Juan Pérez", 5, 1500)

print(f"Nombre del empleado: {empleado.nombre}")
print(f"Antigüedad: {empleado.antiguedad} años")
print(f"Salario base: ${empleado.salario_base}")

bonificacion_general = Empleado.calcular_bonificacion_general()
print(f"Bonificación general: ${bonificacion_general}")

bonificacion_antiguedad = empleado.calcular_bonificacion_antiguedad()
print(f"Bonificación por antigüedad: ${bonificacion_antiguedad}")

bonificacion_total = empleado.calcular_bonificacion_total()
print(f"Bonificación total: ${bonificacion_total}")
