class Usuario:
    def __init__(self, nombre_usuario, contrasena):
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena

# Crear un objeto de la clase Usuario
usuario1 = Usuario("Luis1973", "mi_contraseña_segura")

# Mostrar los atributos del objeto creado
print(f"Nombre de usuario: {usuario1.nombre_usuario}")
print(f"Contraseña: {usuario1.contrasena}")
