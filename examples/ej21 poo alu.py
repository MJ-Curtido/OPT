import math
# Se pone arriba y sirve para definir clases abstractas (interfaz) 
# y métodos abstractos (plantilla base para las figuras)
from abc import ABC, abstractmethod  
# Se pone arriba y sirve para definir clases de datos (dataclass)
# son clases simples que sirven sobre todo para almacenar datos
from dataclasses import dataclass


# ==============================================================================
# CLASE ABSTRACTA (Interfaz / Plantilla base para las figuras)
# no se pueden crear objetos de esta clase, solo sirve para heredar de ella
# ==============================================================================
class Figura(ABC):
    @abstractmethod
    # el método calcular_area() es abstracto, lo que significa que las clases hijas deben implementarlo
    # se crea sin código, solo con pass, para obligar a las clases hijas a implementarlo
    # no se definen parámetros, porque cada figura puede tener los suyos propios 
    # (Círculo: radio, Rectángulo: ancho y alto, etc)
    def calcular_area(self):
        # pass no hace nada, instrucción nula, necesaria para mantener la indentación y sintaxis correcta
        # se usa en 3 casos: 
        # como en este caso, para definir un método abstracto que no tiene implementación en la clase base
        # para planificar estructuras de control (if, for, while) que aún no tienen código
        # para crear clases vacías que aún no tienen atributos ni métodos, por ejemplo: clase personalizada
        # que hereda de otra clase y aún no tiene ni atributos ni métodos propios, o incluso nunca va a tenerlos.

        pass    

# ==============================================================================
# CLASE BASE COMPLETA (Atributos, Encapsulación, Properties y Métodos Especiales)
# ==============================================================================

class Punto:
    # A. ATRIBUTO DE CLASE: Compartido por todas las instancias (Contador global)
    Z = 0
    total_puntos = 0

    # los __ solo se ponen dentro de la clase, no en las llamadas desde el programa principal
    # el __init__ es un método especial que se llama automáticamente al crear un objeto de la clase
    # no hay que llamarlo explícitamente, se llama automáticamente al crear un objeto de la clase
    # por ejemplo: p1 = Punto(3, 5) llama automáticamente a p1.__init__(3, 5)
    # En Python, el "constructor" habitual (__init__) no es la función que crea el objeto, 
    # sino la que lo inicializa (le asigna las variables y valores iniciales).
    # El proceso cuando haces variable = Punto(3, 4):
        # Paso 1 (Creación): Python ejecuta un método especial previo llamado __new__. 
        # Este método es el que reserva el espacio en la memoria RAM y crea la instancia vacía.
        # Paso 2 (Inicialización): Una vez que esa instancia vacía ya existe en memoria, 
        # Python se la pasa automáticamente a __init__ como el primer argumento: self.
    # Por lo tanto, cuando entras al bloque de código de __init__, el objeto YA EXISTE en la memoria RAM; simplemente está "vacío", esperando a que le asignes sus atributos (
    def __init__(self, x, y):
        # Atributos de instancia privados por convención ('_')
        # ojo se puede acceder a ellos desde fuera de la clase, pero no es buena práctica
        self._x = float(x)
        self._y = float(y)

        # los privados estrictos se definen con doble guión bajo '__', pero no es necesario en este caso

        # los publicos no llevan guión bajo, pero no es buena práctica ponerlos públicos, 
        # porque se pueden modificar desde fuera de la clase sin control
        
        # Incrementamos el contador global cada vez que se instancia un Punto
        Punto.total_puntos += 1

    # --------------------------------------------------------------------------
    # ENCAPSULACIÓN 1: Estilo tradicional (get_x / set_x)
    # Getter y Setter para Encapsulación, se definen con _x y _y para indicar que son privados, 
    # pero se accede a ellos mediante métodos públicos: get para leer y set para modificar
    # aclaración: en Python no hay encapsulación real, es solo una convención, pero es buena práctica 
    # seguirla
    # otra aclaración: al iniciar el objeto se accede directamente a los atributos privados
    # por ejemplo: p1 = Punto(3, 5) no hay que poner p1.set_x(3) y p1.set_y(5), se hace directamente 
    # en el constructor
    # --------------------------------------------------------------------------
    
    def get_x(self):
        # Formatea el número a 1 decimal (ej: 5 -> "5.0", 3.14159 -> "3.1"). Obligamos a leer 
        # con get al ser un atributo privado y de esta forma controlamos que se lea con un decimal, 
        # aunque internamente sea un float con más decimales
        return f"{self._x:.1f}"

    def set_x(self, nuevo_x):
        # Filtro: si está fuera de rango, no lo guarda
        # obligamos a escribir con set al ser un atributo privado y de esta forma controlamos 
        # el valor de entrada
        if nuevo_x < -100 or nuevo_x > 100:
            print("Error: X debe estar entre -100 y 100")
        else:
            self._x = float(nuevo_x)

    # --------------------------------------------------------------------------
    # ENCAPSULACIÓN 2: Estilo Pythonic (@property y @y.setter)
    # Permite acceder como 'p.y' en lugar de usar funciones get/set
    # @property marca el método como la puerta de salida (lectura).
    # @<nombre>.setter marca el método como la puerta de entrada
    # --------------------------------------------------------------------------
    @property
    def y(self):
        """Getter para Y: devuelve el valor redondeado a 1 decimal"""
        return round(self._y, 1)

    @y.setter
    def y(self, nuevo_y):
        """Setter para Y: valida rango al hacer 'p.y = valor'"""
        if nuevo_y < -100 or nuevo_y > 100:
            print("Error: Y debe estar entre -100 y 100")
        else:
            self._y = float(nuevo_y)

    # --------------------------------------------------------------------------
    # MÉTODOS DE INSTANCIA Y MÉTODOS DE CLASE (@classmethod)
    # self (Método de instancia): "Hablo de MÍ MISMO y de MIS propios datos" 
    # (ej. "mover este punto", "calcular el área de este círculo").
    # cls (Método de clase): "Hablo de la FABRICA/PLANTILLA entera" 
    # (ej. "crear un punto desde un texto", "saber cuántos puntos hemos fabricado en total").
    # --------------------------------------------------------------------------
    
    def distancia_al_origen(self):
        """Calcula la distancia euclidiana desde (0,0)"""
        # es un método de instancia, porque depende de los atributos de la instancia (self._x, self._y)
        return round(math.sqrt(self._x**2 + self._y**2), 2)

    @classmethod
    def crear_desde_cadena(cls, texto):
        """Constructor alternativo: Recibe '3.5, 4.2' y devuelve un nuevo Punto"""
        # el primer argumento de un método de clase se llama cls por convención, y representa 
        # la clase en sí misma, ya que el objeto aún no existe. 
        # en el caso del __init__, el primer argumento se llama self, porque se ejecuta 
        # sobre un objeto ya creado, al ejecutarse el __new__ previamente (Python lo hace internamente).
        # es un método de clase, porque no depende de los atributos de una instancia concreta, 
        # sino de la clase en general
        # en este caso no depende de un atributo de clase, pero podría depender de otros 
        # atributos de clase si los hubiera
        # Estándar de la comunidad (PEP 8): La guía oficial de estilo de Python establece que:
            # El primer argumento de un método normal de instancia y del constructor principal
            # debe llamarse self.
            # El primer argumento de un método de clase (@classmethod) debe llamarse cls.
        x_str, y_str = texto.split(",")
        return cls(float(x_str), float(y_str))

    # --------------------------------------------------------------------------
    # MÉTODOS ESPECIALES / MÁGICOS (Dunder Methods)
    # No se invocan directamente desde fuera; Python los activa automáticamente 
    # mediante operadores o funciones nativas.
    # --------------------------------------------------------------------------

    # __str__: Salida limpia para print(punto) y str(punto)
    def __str__(self):
        return f"P({round(self._x, 1)}, {self.y})"

    # __repr__: Representación técnica para objetos dentro de listas print([p1, p2])
    # Se suele definir igual que __str__, pero se puede personalizar para mostrar más información
    # por ejemplo, para mostrar el nombre de la clase y los atributos internos
    # se usa obligatoriamente en la consola interactiva, pero no en print() ni str()
    # y tambien en las listas, diccionarios y tuplas, cuando se imprimen en pantalla
    # es más completo que __str__, por tanto, es mejor definirlo en lugar de __str__
    # en el ejemplo siguiente, se define igual que __str__, pero no es lo común.
    def __repr__(self):
        return self.__str__()

    # __eq__: Permite comparar p1 == p2 por sus atributos y no por memoria
    def __eq__(self, otro):
        return self._x == otro._x and self._y == otro._y

    # __lt__: Criterio de ordenación para sort() y sorted() (Compara X, desempata con Y)
    def __lt__(self, otro):
        if self._x == otro._x:
            return self._y < otro._y
        return self._x < otro._x

    # --------------------------------------------------------------------------
    # MÉTODOS ESTÁTICOS (@staticmethod)
    # No llevan ni 'self' ni 'cls' porque son funciones puramente "herramienta"
    # al programar con clases se suelen meter estos métodos dentro de una clase
    # sólo por organización, aunque no dependan de la instancia ni de la clase.
    # en python se pueden poner fuera de la clase, definidos en el main o no.
    # más abajo pongo un ejemplo de función que no está en ninguna clase ni en el main, 
    # pero que se puede usar igual que un método estático.
    # por lo tanto, repito, usar metodos estaticos dentro de una clase es solo por organización.
    # --------------------------------------------------------------------------

    @staticmethod
    def es_coordenada_valida(val):
        """
        Es un filtro previo para validar coordenadas antes de crear un Punto o modificarlo.
        1. ¿Es realmente un número? (int o float)
        2. ¿Está dentro del rango permitido? (entre -100 y 100)
        
        Devuelve True (si es válido) o False (si es incorrecto).
        """
        
        # PASO 1: Comprobar si 'val' es un número entero (int) o decimal (float)
        # isinstance(variable, tipo) comprueba si una variable es del tipo de dato indicado.
        # Devuelve True si coincide y False si no.
        # Tip: Pasar una tupla (int, float) permite validar varios tipos a la vez.
        es_numero = isinstance(val, (int, float))
        
        # PASO 2: Comprobar si el número está en el rango [-100, 100]
        # Nota: Si 'val' no es número, esta comparación daría error, por eso
        # Python evalúa primero 'es_numero'. Si es False, ni siquiera mira el rango.
        en_rango = -100 <= val <= 100 if es_numero else False
        
        # PASO 3: Devuelve True solo si cumple AMBAS condiciones
        return es_numero and en_rango

# ==============================================================================
# CLASE DE DATOS (Dataclass)
# genera automáticamente __init__, __repr__ y __eq__
# ==============================================================================

@dataclass
class PuntoSimple:
    x: float
    y: float

# ==============================================================================
# Gestión de memoria optimizada con __slots__
# Por defecto, Python guarda los atributos de cada objeto en un diccionario interno (self.__dict__). 
# Si vas a crear millones de puntos, puedes usar __slots__ para restringir los atributos 
# fijamente y ahorrar hasta un 60-70% de memoria RAM.
# En ese diccionario guarda los nombres de los atributos como texto (claves) y sus valores asignados.
# de esta forma: en un objeto (p) de la clase normal Punto, podemos poner:
# print(p.__dict__)  
# Salida en pantalla: {'x': 3, 'y': 4}
# además, podemos añadir atributos nuevos a ese objeto en tiempo de ejecución:
# p.z = 5
# y ahora p.__dict__ devuelve: {'x': 3, 'y': 4, 'z': 5}
# Esto es muy flexible, pero ocupa memoria extra.   
# ==============================================================================

class PuntoOptimizado:
    __slots__ = ('_x', '_y')  # Evita la creación del diccionario interno __dict__
    
    def __init__(self, x, y):
        self._x = x
        self._y = y

# ==============================================================================
# HERENCIA (Relación "Es un")
# ==============================================================================

class PuntoConNombre(Punto):
    def __init__(self, x, y, nombre):
        # super() invoca al constructor de Punto (la clase padre)
        super().__init__(x, y)
        self.nombre = nombre

    def __str__(self):
        return f"{self.nombre}{super().__str__()}"


# ==============================================================================
# COMPOSICIÓN (Relación "Tiene un")
# ==============================================================================

class Circulo(Figura):
    def __init__(self, x, y, radio):
        # Composición: El Círculo 'tiene un' Punto como su centro
        self.centro = Punto(x, y)
        self.radio = radio

    def calcular_area(self):
        return round(math.pi * (self.radio ** 2), 2)

    def __str__(self):
        return f"Círculo con centro en {self.centro} y radio {self.radio}"
    

# ==============================================================================
# Polimorfimo: Función que acepta cualquier objeto que tenga ese método
# en este caso cualquier objeto que tenga el método .calcular_area() (Círculo, Rectángulo, etc)
# Diferentes clases pueden tener métodos con el mismo nombre, y tú puedes llamar a ese método 
# sin preocuparte de qué clase exacta es el objeto, la llamada a la función no necesita argumentos, 
# en la definición de la llamada se pone (self)
# Para este tipo de polimorfismo, no hace falta que las clases tengan un ancestro común,
# pero en este ejemplo se ha puesto la clase abstracta Figura como ancestro común,
# ==============================================================================

class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    def calcular_area(self):
        return self.ancho * self.alto

# Función polimórfica: acepta cualquier objeto que tenga el método .calcular_area()
# esta función se puede poner fuera de la definición de las clases y fuera del main
# cosa que no se puede hacer en otros lenguajes de programación, pero en Python sí, 
# porque es un lenguaje dinámico

def imprimir_area(figura):
    print(f"El área es: {figura.calcular_area():.2f}")

# ==============================================================================
# CLASE AUXILIAR
# ==============================================================================
class Coloreable:
    def __init__(self, color="Rojo"):
        self.color = color

    def pintar(self, nuevo_color):
        self.color = nuevo_color


# ==============================================================================
# HERENCIA MÚLTIPLE, donde RectanguloColoreado hereda de Rectangulo y Coloreable
# se ponen las dos clases entre paréntesis, separadas por comas
# ==============================================================================
class RectanguloColoreado(Rectangulo, Coloreable):

    def __init__(self, ancho, alto, color="Rojo"):
        # Un solo super() se encarga de llamar a AMBAS clases en el orden correcto
        super().__init__(ancho=ancho, alto=alto, color=color)

# ==============================================================================
# DEMOSTRACIÓN COMPLETA EN EL PROGRAMA PRINCIPAL
# ==============================================================================
# __name__ es el estándar en Python para distinguir cuándo un archivo se ejecuta directamente 
#  y cuándo se importa desde otro sitio.
# de esta forma el mismo código sirve para ejecución directa como un programa principal main y sirva
# también para importación desde otro módulo, se pone todo el código principal dentro de este bloque if
# Cuando un archivo .py se ejecuta directamente, Python asigna a __name__ el valor "__main__".
# Cuando se importa desde otro archivo, __name__ toma el valor del nombre del archivo (sin extensión .py), con
# lo que el bloque if no se ejecuta y no se imprime nada en pantalla, pero sí se pueden usar las clases 
# y funciones definidas en ese archivo.

if __name__ == "__main__":
    print("--- 1. Getters y Setters Tradicionales vs @property ---")
    p1 = Punto(3.14159, 4.567)
    
    # Lectura
    print("X con get_x():", p1.get_x())     # Usando get_x() tradicional -> "3.1"
    print("Y con @property:", p1.y)         # Usando @property nativo  -> 4.6
    
    # Escritura con validación
    p1.set_x(150)                           # Falla por filtro
    p1.y = 200                              # Falla por filtro de @y.setter
    
    p1.set_x(10)                            # Válido
    p1.y = 20                               # Válido
    print("Punto actualizado:", p1)         # Muestra: P(10.0, 20.0)

    print("\n--- 2. Métodos Propios y Constructor @classmethod ---")
    p_origen = Punto(3, 4)
    print("Distancia al origen:", p_origen.distancia_al_origen()) # 5.0
    
    p_texto = Punto.crear_desde_cadena("10.5, 20.2")
    print("Punto creado desde texto:", p_texto) # P(10.5, 20.2)

    print("\n--- 3. Métodos Mágicos (__eq__, __lt__, __repr__) ---")
    p2 = Punto(5, 5)
    p3 = Punto(5, 5)
    print("¿Son p2 y p3 iguales (==)?:", p2 == p3) # True por __eq__

    lista_puntos = [Punto(8, 1), Punto(2, 9), Punto(2, 3)]
    lista_puntos.sort() # Ordena usando __lt__
    print("Lista ordenada:", lista_puntos) # Muestra representaciones bonitas por __repr__

    print("\n--- 4. Herencia y Composición ---")
    pn = PuntoConNombre(0, 0, "Origen")
    print("Herencia:", pn) # OrigenP(0.0, 0.0)

    c = Circulo(2, 3, 5)
    print("Composición:", c)
    print("Área del círculo:", c.calcular_area())

    print("\n--- 5. Atributo de Clase (Contador global) ---")
    print("Total de puntos instanciados en la sesión:", Punto.total_puntos)

    # Funciona igual para Círculo o Rectángulo sin importar de dónde hereden
    imprimir_area(Circulo(0, 0, 5))
    imprimir_area(Rectangulo(4, 6))

    # crea un objeto de RectanguloColoreado, que hereda de Rectangulo y Coloreable
    r_coloreado = RectanguloColoreado(4, 6, "Azul")

    print(r_coloreado.calcular_area())  # Usa el método calcular_area de la clase Rectangulo
    print(r_coloreado.color)            # Usa el método pintar de la clase Coloreable

    # creamos un objeto de la clase PuntoSimple, que es una dataclass
    # podemos poner print(p) directamente porque la dataclass genera automáticamente el método __repr__
    p = PuntoSimple(3.0, 4.0)
    print(p)  # Muestra: PuntoSimple(x=3.0, y=4.0)