import os  # Módulo para manejo de archivos y rutas
import os.path

ficheronuevonombre="./UltimoNombre.txt"
nuevonombre=""
# verifico si el archivo existe y lo abro
if os.path.exists(ficheronuevonombre):
    with open(ficheronuevonombre, "r") as fichero:
        nuevonombre=fichero.readline()
fichero.close()

nombrenumerico=int(nuevonombre[1:])

contenido = os.listdir("D:/Cambio de Nombre")
cantidadficheros=len(contenido)
#nombrenumerico+=1
#Renombrar los archivos
i=0
while i < cantidadficheros:
    nombrefichero=contenido[i]
    extension = os.path.splitext(nombrefichero)
    contenido[i] = "a" + str(nombrenumerico) + str(extension[1])
    nombrenumerico+=1
    i+=1

i=0
contenidoarenombrar = os.listdir("D:/Cambio de Nombre")
while i < cantidadficheros:
    os.rename("D:/Cambio de Nombre/" + contenidoarenombrar[i], "D:/Cambio de Nombre/" + contenido[i])
    i+=1

with open(ficheronuevonombre, "w") as fichero:
    fichero.write("a" + str(nombrenumerico))
fichero.close()

print(contenidoarenombrar) 
print(contenido)
print(cantidadficheros)