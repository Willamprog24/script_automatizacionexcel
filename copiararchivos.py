import os
import shutil

contenidos = os.listdir("Z:\\ListadosSeguimientos")


for elemento in contenidos:
    try:
        print(f"Copiando {elemento} --> {contenidos} ... ", end="")
        src = os.path.join("Z:\\ListadosSeguimientos", elemento) # origen
        dst = os.path.join("C:\\Listados", elemento) # destino
        shutil.copy(src, dst)
        print("Correcto")
    except:
        print("Falló")
        print("Error, no se pudo copiar el archivo. Verifique los permisos de escritura")
        
        