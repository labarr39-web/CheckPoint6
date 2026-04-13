
## CheckPoint 6

  

<br><br>

  

1.  ***¿Para qué usamos Clases en Python?***

  

<br>

En Python, las clases y los objetos trabajan juntos para organizar y gestionar datos. Se crea una clase para definir comportamientos compartidos, después se crean objetos que usen esos comportamientos.
<br>

En otras palabras, una clase es como un plano o plantilla que se utiliza para crear objetos.
<br>

Pero vayamos por partes...  
 En primer lugar veamos qué son las clases y cómo usarlas para crear objetos.
<br>

Una clase es un contenedor, el cual alberga datos y funciones que definirá el comportamiento de los objetos que se creen.
<br>

Para crear una clase se usa la palabra clave `class`  seguida del nombre de la clase y dos puntos (`:`).   
Después, dentro de la clase, se puede añadir un inicializador además de cualquier atributo y método.  
<br>  

Los atributos son como variables dentro de una clase y se usan para almacenar datos. Los métodos son funciones definidas dentro de una clase y son las acciones que pueden realizar los objetos creados con una clase .  
<br>  

A continuación se muestra la sintáxis básica de una clase:  

    class NombreClase:
		    def __init__(self, nombre, edad):
				    self.nombre = nombre
				    self.edad = edad

				def ejemplo_metodo(self):
						print(self.nombre.upper())
				

* `class NombreClase` se compone de la palabra clave `class` para crear una clase, seguida del nombre de la clase, en este caso `NombreClase`.  
<br>  
Para los nombres de clase en Python (y en otros lenguajes) se suele usar la forma 'CamelCase', donde el nombre comienza en mayúsculas, y en caso de formarse con varias palabras se escriben todas capitalizadas y juntas (sin guiones bajos).  

<br>  

* `def __init__(self, nombre, edad)` es el método especial que es llamado automáticamente cuando se crea un nuevo objeto.  


	Inicializa los atributos de los objetos que serán creados con la clase. Además de eso, el primer parámetro de `__init__`  siempre es una referencia  al objeto específico que se está creando o usando. Por convención, este parámetro se llama `self`, pero técnicamente, puede usarse cualquier nombre. `self` permite acceder a los propios atributos y métodos del objeto.  
	<br>  
	
* `self.nombre = nombre` y `self.edad = edad` son los atributos que van a tener los objetos.  
	<br>  
	
* `def ejemplo_metodo(self):` es el método que cada objetos creado puede llamar.  
	<br>  
	
* `print(self.nombre.upper())` es lo que hará el método `ejemplo_metodo`, en este caso, imprime nombre en mayúsculas.  
<br>  

Veámoslo ahora con un ejemplo y cómo se pueden creare objetos a partir de una clase:  

    class Perro:
		    def __init__(self, nombre, edad):
				    self.nombre = nombre
				    self.edad = edad

				def ladrar(self):
						print(f'{self.nombre.upper()} dice ¡guau guau!')
						
<br>  

Con esta clase `Perro` vamos a crear objetos.  

Esta es la sintaxis básica para  crear objetos a partir de una clase:  

    objeto_1 = NombreClase(atributo_1, atributo_2)
    objeto_2 = NombreClase(atributo_1, atributo_2)

<br>  

También se les puede llamar a cualquiera de los métodos definidos en la clase desde cada objeto:  

    objeto_1.nombre_metodo()
    objeto_2.nombre_metodo()
    
<br>  

Ahora vamos con el ejemplo práctico.  

Crearemos dos 'perros' (objetos) usando la clase 'Perro'  

    class Perro:
		    def __init__(self, nombre, edad):
				    self.nombre = nombre
				    self.edad = edad

				def ladrar(self):
					print(f'{self.nombre.upper()} dice ¡guau guau, y tengo {self.edad} años!')
		
		
	# Inicializamos perro_1 y perro_2
	
	perro_1 = Perro('Yoshi', 3)
	perro_2 = Perro('Casper', 7)
	
	
	# Llamamos al metodo ladrar
	  
	perro_1.ladrar() # YOSHI dice ¡guau guau, y tengo 3 años!
	perro_2.ladrar() # CASPER dice ¡guau guau, y tengo 7 años!

Hemos creado `perro_1` y `perro_2` pasándoles 2 argumentos a cada uno, Yoshi y 3 al primero, y Casper y 7 al segundo; con lo que se establecen los atributos `nombre` y `edad` para estas instancias.

<br>  
Al llamar al método `ladrar()` podemos comprobar que las salidas son distintas aunque se hayan usando los mismos atributos `nombre` y `edad` en ambos casos.  

<br>  
Resumiendo:  

Una clase define qué datos y comportamiento debe tener un objeto, y este último contiene los datos reales y usa dicho comportamiento.  

La clase se escribe una vez, y se pueden crear muchos objetos a partir de ella, cada uno con datos diferentes.

<br><br>  

2. ***¿Qué método se ejecuta automáticamente cuando se crea una instancia de una clase?***

    <br>
    Respuesta
    <br><br>  
    
3. ***¿Cuáles son los tres verbos de API?***

    <br>
    Respuesta
    <br><br>  
    
4. ***¿Es MongoDB una base de datos SQL o NoSQL?***

    <br>
    Respuesta
    <br><br>  
    
5. ***¿Qué es una API?***

    <br>
    Respuesta
    <br><br>  
    
6. ***¿Qué es Postman?***

    <br>
    Respuesta
    <br><br>  
    
7. ***¿Qué es el polimorfismo?***

    <br>
    Respuesta
    <br><br>  
    
8. ***¿Qué es un método dunder?***

    <br>
    Respuesta
    <br><br>  
    
9. ***¿Qué es un decorador de python?***

    <br>
    Respuesta
    <br><br>  
    