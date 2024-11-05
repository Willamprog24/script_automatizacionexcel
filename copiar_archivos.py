import os
import re
import shutil
import todo
from datetime import datetime
import xlwings as xw
import time
import win32com.client
import correrbat as bat



#rutas de archivos txt
ruta_origen = 'Z:\ListadosSeguimientos'
ruta_destino = 'C:\\Listados'
prefijo_cr = 'CR'

#archivo de excel

ruta_principal = 'Z:\\2. SEGUIMIENTO DIARIO P.O\Seguimiento diario\CR\\2024'
 
# Obtiene la lista de todas las carpetas en la ruta principal
carpetas_principal = [carpeta for carpeta in os.listdir(ruta_principal) if os.path.isdir(os.path.join(ruta_principal, carpeta))]
 
# Ordena las carpetas alfabéticamente
carpetas_principal.sort()
 
# Accede a la última carpeta
ultima_carpeta = os.path.join(ruta_principal, carpetas_principal[-1])
# Obtiene la lista de todas las carpetas dentro de la última carpeta
print(ultima_carpeta)
# Obtiene la lista de todos los archivos en la última subcarpeta

lista = os.listdir(ultima_carpeta)
archivos_ultima_carpeta = sorted(lista, key= lambda x: os.path.getmtime(os.path.join(ultima_carpeta, x)))

ultimo_archivo_excel = archivos_ultima_carpeta[-1]
print(archivos_ultima_carpeta)

# Copia el último archivo de Excel a una nueva ubicación

fecha_Actual = datetime.now().strftime("%d-%m-%y")
print(fecha_Actual)
nuevo_nombre_Excel = f'Seguimiento diario {fecha_Actual} CR PRUEBA.xlsm'
print(nuevo_nombre_Excel)
ruta_nuevo_nombre_Excel = os.path.join(ruta_destino,nuevo_nombre_Excel)

archivos_cr_copiar = [archivo for archivo in os.listdir(ruta_origen) if archivo.startswith(prefijo_cr) ]

if todo.grantotal is True:
    for archivo in archivos_cr_copiar:
        shutil.copy2(os.path.join(ruta_origen,archivo),os.path.join(ruta_destino,archivo))
        shutil.copy2(os.path.join(ultima_carpeta,ultimo_archivo_excel), os.path.join(ruta_destino, ultimo_archivo_excel,ruta_nuevo_nombre_Excel))
        
#archivo renombrado , quitar los datos de la hoja programa y quitar agrupaciones y filtros.
archivo_local = os.path.join(ruta_destino,nuevo_nombre_Excel)

app = xw.App()
WB = xw.books.open(archivo_local)

    
  
print("Paso")
print(WB)

Hoja_programa = WB.sheets['Programa']
Hoja_programa.range('A2:BV500').clear_contents()


nombres_hojas = [hoja.name for hoja in WB.sheets]
print(nombres_hojas)
permitidos = ['Prod. Nivel', 'Prod. ContPed', 'No Programable', 'Cancelaciones']
for nombre in nombres_hojas:
    if nombre in permitidos:
        hoja = WB.sheets[nombre]
        print(hoja)
        hoja.api.AutoFilterMode = False
        hoja.api.Columns.Hidden = False

# Guarda el archivo antes de ejecutar la macro


# Ejecuta la macro
WB.macro("ejecutar").run()



# Elimina los nombres "Criterios" y "Extract"

WB.save()
# Cierra la aplicación de Excel
WB.close()
app.quit()

# Copia el archivo modificado
shutil.copy2(os.path.join('C:\Listados', nuevo_nombre_Excel), os.path.join(ultima_carpeta, nuevo_nombre_Excel))

print(ruta_destino, ultima_carpeta)