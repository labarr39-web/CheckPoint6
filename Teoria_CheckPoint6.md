
# CheckPoint 6

<br>  

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

A continuación se muestra la sintaxis básica de una clase:  

```python
 class NombreClase:
	 def __init__(self, nombre, edad):
	    self.nombre = nombre
	    self.edad = edad

	 def ejemplo_metodo(self):
			print(self.nombre.upper())
```				

* `class NombreClase` se compone de la palabra clave `class` para crear una clase, seguida del nombre de la clase, en este caso `NombreClase`.  
<br>  
Para los nombres de clase en Python (y en otros lenguajes) se suele usar la forma 'CamelCase', donde el nombre comienza en mayúsculas, y en caso de formarse con varias palabras se escriben todas capitalizadas y juntas (sin guiones bajos).  

<br>  

* `def __init__(self, nombre, edad)` es el método especial que es llamado automáticamente cuando se crea un nuevo objeto.  


	Inicializa los atributos de los objetos que serán creados con la clase.
	<br>  
	
* `self.nombre = nombre` y `self.edad = edad` son los atributos que van a tener los objetos.  
	<br>  
	
* `def ejemplo_metodo(self):` es el método que cada objeto creado puede llamar.  
	<br>  
	
* `print(self.nombre.upper())` es lo que hará el método `ejemplo_metodo`, en este caso, imprime nombre en mayúsculas.  
<br>  

Veámoslo ahora con un ejemplo y cómo se pueden creare objetos a partir de una clase:  

```python
class Perro:
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad

def ladrar(self):
		print(f'{self.nombre.upper()} dice ¡guau guau!')
```
<br>  

Con esta clase `Perro` vamos a crear objetos.  

Esta es la sintaxis básica para  crear objetos a partir de una clase:  

```python
objeto_1 = NombreClase(atributo_1, atributo_2)
objeto_2 = NombreClase(atributo_1, atributo_2)
```

<br>  

También se les puede llamar a cualquiera de los métodos definidos en la clase desde cada objeto:  

```python
    objeto_1.nombre_metodo()
    objeto_2.nombre_metodo()
```

<br>  

Ahora vamos con el ejemplo práctico.  

Crearemos dos 'perros' (objetos) usando la clase 'Perro'  

```python
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
```

Hemos creado `perro_1` y `perro_2` pasándoles 2 argumentos a cada uno, Yoshi y 3 al primero, y Casper y 7 al segundo; con lo que se establecen los atributos `nombre` y `edad` para estas instancias.

<br>  
Al llamar al método `ladrar()` podemos comprobar que las salidas son distintas aunque se hayan usando los mismos atributos `nombre` y `edad` en ambos casos.  

<br>  
Resumiendo:  

Una clase define qué datos y comportamiento debe tener un objeto, y este último contiene los datos reales y usa dicho comportamiento.  

La clase se escribe una vez, y se pueden crear muchos objetos a partir de ella, cada uno con datos diferentes.  

<br><br>

2.  ***¿Qué método se ejecuta automáticamente cuando se crea una instancia de una clase?***

  <br>
  
  Tal y como se mostró en el punto anterior
`__init__` es un método constructor al que se llama justo después de crearse un objeto (instancia) de una clase.  

 Su función principal es inicializar los atributos del objeto con los valores que se le pasen o con valores por defecto.  

Su sintaxis básica es:  

```python
    class MiClase:
    def __init__(self, parametros):
        # Inicialización de atributos
        self.atributo = valor
```

<br>  

Al asignar una clase a un objeto  

    objeto = MiClase(argumentos)
  
  <br>  
  
  Python crea el objeto y automáticamente llama al método `__init__` con los argumentos que se le haya pasado.  

Aquí tenemos un ejemplo:  

```python
    class Persona:
		    def __init__(self, nombre, edad):
		        self.nombre = nombre
		        self.edad = edad  
		        
	p = Persona("Ana", 30)  
	print(p.nombre)  # Salida: Ana  
	print(p.edad)    # Salida: 30
  ````
  
  <br>  
  
Además de eso, el primer parámetro de `__init__`  siempre es una referencia  al objeto específico que se está creando o usando. Por convención, este parámetro se llama `self`, pero técnicamente, puede usarse cualquier nombre. `self` permite acceder a los propios atributos y métodos del objeto.  

<br><br>

3.  ***¿Cuáles son los tres verbos de API?***

  <br>
  
  Antes de explicar los tres verbos de API, creo que es conveniente empezar indicando **qué es una API**:  

Una  **API**  o "Interfaz de Programación de Aplicaciones"  por sus siglas en inglés, es un conjunto de reglas que permite que dos programas o sistemas diferentes se comuniquen entre sí.

Lo mejor para entenderlo va a ser utilizar un símil.

Haciendo un alarde de imaginación vamos a transformar el servidor al que queremos acceder en un restaurante.

Nada más entrar nos atiende un camarero muy amable, que en nuestro caso sería la API.  

Nosotros le decimos qué queremos pedir (hacemos una solicitud); entonces el camarero entra en la cocina (el sistema o servidor) con nuestro pedido, y vuelve con la comida (la respuesta).  

Nosotros no necesitamos saber cómo se elabora la comida, tan sólo saber cómo pedirla.

En el mundo digital, las APIs permiten que aplicaciones, sitios web o dispositivos intercambien información y realicen acciones sin que el usuario tenga que intervenir directamente en el proceso.  
<br>   
Una vez dicho esto comencemos por saber qué son los verbos de una API:  

Si hablamos de APIs, especialmente las que usan el estilo REST (muy comunes en la web), se utilizan **verbos HTTP** para indicar qué acción queremos hacer con un recurso (un dato o conjunto de datos).  

Los tres verbos principales son:  

	    - GET  
	    - POST  
	    - PUT  
	    
<br>  
Para los ejemplos vamos a usar una biblioteca ficticia y cuya API tiene los siguientes endpoints para los libros:  

		GET /libros      -> lista todos los libros  
		GET /libros/{id} -> obtiene un libro po ID  
		POST /libros     -> crea un libro nuevo  
		PUT /libros/{id} -> actualiza un libro por ID  

<br>  

 * **GET (Obtener)**  
 
 <br>  
 
|¿Qué hace?|Ejemplo sencillos |En términos API|
|--|--|--|
| Pide información o datos de un recurso | Queremos ver una lista de libros en una biblioteca| Se solicita los datos de los libros para que los muestre |  

<br>  
Supongamos que queremos obtener una lista de libros.
  
<br> 

```python
    import requests

	url = "https://api.biblioteca.com/libros"
	response = requests.get(url)

	if response.status_code == 200:
	    libros = response.json()
	    print("Lista de libros:")
	    for libro in libros:
	        print(f"- {libro['titulo']} por {libro['autor']}")
	else:
	    print("Error al obtener libros:", response.status_code)
```

  <br>  
  Esto imprime la lista de libros, pero si lo que queremos es obtener un libro en concreto lo buscamos por su id, que es único.
    
   <br>  
    
 ```python
 
    import requests

	libro_id = 123
	url = f"https://api.biblioteca.com/libros/{libro_id}"
	response = requests.get(url)

	if response.status_code == 200:
	    libro = response.json()
	    print(f"Libro: {libro['titulo']} por {libro['autor']}")
	else:
	    print("Libro no encontrado o error:", response.status_code)
```

<br>  
Así sólo imprimirá los datos de un único libro, si lo encuentra.

<br>  

* **POST (Crear)**  
 
 <br>  
 
|¿Qué hace?|Ejemplo sencillos |En términos API|
|--|--|--|
| Envía datos para crear un nuevo recurso | Queremos agregar un nuevo libro a la biblioteca| Se envía la información del libro para que se agregue a la base de datos |  

<br>  
Queremos añadir un libro nuevo:  

<br>  

```python
	import requests

	url = "https://api.biblioteca.com/libros"
	
	# Este es el nuevo libro que queremos añadir
	
	nuevo_libro = {
	    "titulo": "Cien años de soledad",
	    "autor": "Gabriel García Márquez",
	    "año": 1967,
	    "genero": "Realismo mágico"
	}

	response = requests.post(url, json=nuevo_libro)

	if response.status_code == 201:
	    libro_creado = response.json()
	    print("Libro creado:", libro_creado)
	else:
	    print("Error al crear libro:", response.status_code)
```

<br>  


* **PUT (Actualizar)**  
 
 <br>  
 
|¿Qué hace?|Ejemplo sencillos |En términos API|
|--|--|--|
| Actualiza un recurso existente o lo crea si no existe | Queremos corregir el título de un libro que ya está en la biblioteca| Se envían los datos actualizados para que se modifique el recurso |  

<br>  
Queremos actualizar el título del libro con id 123:  

<br>  

```python

    import requests

	libro_id = 123
	url = f"https://api.biblioteca.com/libros/{libro_id}"
	libro_actualizado = {
	    "titulo": "Cien años de soledad (Edición revisada)",
	    "autor": "Gabriel García Márquez",
	    "año": 1967,
	    "genero": "Realismo mágico"
	}

	response = requests.put(url, json=libro_actualizado)

	if response.status_code == 200:
	    libro = response.json()
	    print("Libro actualizado:", libro)
	else:
	    print("Error al actualizar libro:", response.status_code)
```

<br>  

Los códigos de estado pueden variar según la API, per 200 (OK), 201 (Creado) y 204 (Sin contenido) son los más comunes para éxito.  

El formato JSON en los ejemplos es típico para APIs REST.
    
Estos son los tres verbos más comunes, aunque existen más como DELETE (Eliminar) y PATCH (Actualizar parcialmente), entre otros.  

<br><br>  

4.  ***¿Es MongoDB una base de datos SQL o NoSQL?***  

<br>  

   [MongoDB](https://www.mongodb.com) es un sistema de gestión de bases de datos NoSQL, orientado a documentos y de código abierto.  

A diferencia de las bases de datos relacionales tradicionales que usan tablas y filas, MongoDB almacena la información en documentos flexibles con formato JSON, lo que le da gran escalabilidad y flexibilidad.

Algunas características clave de MongoDB son:

Utiliza documentos en lugar de tablas, lo que facilita manejar datos semiestructurados o con esquemas variables.  

Ofrece un modelo avanzado de consultas e indexación.  

Es muy escalable y adecuado para aplicaciones que requieren manejar grandes volúmenes de datos o datos heterogéneos.  

Es ampliamente usado en desarrollo web, big data y aplicaciones modernas que necesitan rapidez y flexibilidad en el manejo de datos.  

En resumen, MongoDB es una base de datos NoSQL orientada a documentos que facilita el almacenamiento y consulta de datos de forma flexible y escalable.  
<br>  

Ahora veamos algunos ejemplos de cómo usar  MongoDB con Python, para ello vamos a importar la biblioteca pymongo.

* Lo primero es conectarse a MongoDB  

```python
	import pymongo 
	# Crear cliente MongoDB (por defecto localhost:27017)
	 client = pymongo.MongoClient("mongodb://localhost:27017/") 
	 
	# Seleccionar base de datos
	db = client["mi_base_de_datos"] 
	
	# Seleccionar colección 
	collection = db["mi_coleccion"]
   ```
  
  <br>  
  
  * Ahora insertamos documentos  
  
  ```python
  # Insertar un solo documento
  
documento = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
resultado = collection.insert_one(documento)
print("ID del documento insertado:", resultado.inserted_id)
```  

<br>  

```python
	# Insertar varios documentos
	
documentos = [
    {"nombre": "Ana", "edad": 25, "ciudad": "Barcelona"},
    {"nombre": "Luis", "edad": 35, "ciudad": "Valencia"}
]
resultado = collection.insert_many(documentos)
print("IDs de documentos insertados:", resultado.inserted_ids)
```  

<br>  

* Así podemos consultar documentos  

```python
	# Encontrar un documento
	
persona = collection.find_one({"nombre": "Juan"})
print(persona)
```  
<br>  

```python
	# Encontrar varios documentos
	
personas = collection.find({"edad": {"$gt": 28}})  # edad mayor a 28
for p in personas:
    print(p)
```  

<br>  

* Ahora vamos a actualizar un documento  

<br>  

```python
	# Actualizar un documento
	
resultado = collection.update_one(
    {"nombre": "Juan"},
    {"$set": {"edad": 31}}
)
print("Documentos modificados:", resultado.modified_count)
```  

<br>  

* Por último eliminamos un documento  

<br>  

```python

	# Eliminar un documento
	
	resultado = collection.delete_one({"nombre": "Luis"})
	print("Documentos eliminados:", resultado.deleted_count)
```  

<br>  

Estos son ejemplos básicos para empezar a trabajar con MongoDB desde Python.  

PyMongo ofrece muchas más funcionalidades para consultas avanzadas, agregaciones, índices, etc.  

PyMongo es la biblioteca oficial, pero existen otras, por ejemplo:

- MongoEngine  
- Ming  
- uMongo  
- MincePy  

En la práctica:  

- Driver recomendado: `PyMongo`  
- Para modelos tipo ORM: `MongoEngine`  
- Para async: `PyMongo Async API`  

<br><br>  
4.  ***¿Qué es Postman?***  

<br>  
s
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
    