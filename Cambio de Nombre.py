import os  # Módulo para manejo de archivos y rutas

# Obtener el directorio actual
directorio = os.path.dirname(os.path.abspath(__file__))

# Nombres de archivos relevantes
nombre_script = "Cambio de Nombre.py"
nombre_fichero = "Nombres de Archivo Para Proyecto.txt"

# Ruta del fichero de texto
ruta_fichero = os.path.join(directorio, nombre_fichero)

# Leer nombres desde el fichero de texto
with open(ruta_fichero, "r") as fichero:
    nombres_nuevos = [linea.strip() for linea in fichero]

# Obtener archivos en el directorio excluyendo el script y el fichero de texto
archivos = [archivo for archivo in os.listdir(directorio)
            if archivo not in (nombre_script, nombre_fichero) and os.path.isfile(os.path.join(directorio, archivo))]

# Filtrar solo los archivos que necesitan ser renombrados
archivos_a_renombrar = []
for archivo in archivos:
    nombre_actual = os.path.splitext(archivo)[0]  # Nombre sin extensión
    if nombre_actual not in nombres_nuevos:  # Solo renombrar si el nombre no está en la lista
        archivos_a_renombrar.append(archivo)

# Función para generar un nombre único siguiendo el patrón
def generar_nombre_incremental(base_nombre, numero_inicial, extension, archivos_existentes):
    while True:
        nuevo_nombre = f"{base_nombre}{numero_inicial}"
        nombre_completo = f"{nuevo_nombre}{extension}"
        if nombre_completo not in archivos_existentes:
            return nombre_completo
        numero_inicial += 1

# Generar nombres y renombrar archivos
archivos_existentes = set(os.listdir(directorio))  # Conjunto de archivos actuales
base_nombre = "a"  # Prefijo fijo
numero_inicial = int(nombres_nuevos[-1][1:]) + 1 if nombres_nuevos else 1000000000  # Tomar último número o uno inicial

for archivo in archivos_a_renombrar:
    ruta_antigua = os.path.join(directorio, archivo)
    extension = os.path.splitext(archivo)[1]

    # Generar nombre único incremental
    nuevo_nombre = generar_nombre_incremental(base_nombre, numero_inicial, extension, archivos_existentes)
    numero_inicial += 1
    ruta_nueva = os.path.join(directorio, nuevo_nombre)

    # Renombrar el archivo
    os.rename(ruta_antigua, ruta_nueva)
    archivos_existentes.add(nuevo_nombre)  # Actualizar conjunto
    print(f"{archivo} renombrado a {nuevo_nombre}")

print("Renombrado completado.")