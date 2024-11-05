
import os

ruta_principal = 'Z:\\2. SEGUIMIENTO DIARIO P.O\Seguimiento diario\CR\\2024'

# Obtiene la lista de todas las carpetas en la ruta principal
carpetas_principal = [carpeta for carpeta in os.listdir(ruta_principal) if os.path.isdir(os.path.join(ruta_principal, carpeta))]
 
# Ordena las carpetas alfabéticamente
carpetas_principal.sort()


# Accede a la última carpeta
ultima_carpeta = os.path.join(ruta_principal, carpetas_principal[-1])
# Obtiene la lista de todas las carpetas dentro de la última carpeta

# Obtiene la lista de todos los archivos en la última subcarpeta

lista = os.listdir(ultima_carpeta)
archivos_ultima_carpeta = sorted(lista, key= lambda x: os.path.getmtime(os.path.join(ultima_carpeta, x)))

ultimo_archivo = archivos_ultima_carpeta[-1]
print(archivos_ultima_carpeta)
