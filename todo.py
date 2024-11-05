import os
import re
import shutil
#funciones que validan los archivos
print("Iniciamdo proceso")
#esta funcion lee los archivos l_inv_plan y lexis_rollo_plan

def leer_archivo(rutas):
    resultados = []
    for ruta in rutas:
        with open(ruta,'r',encoding='latin-1') as f:
         lineas = f.readlines()
        if not lineas:
            resultados.append(False)
            continue
        ultima_linea = lineas[-1].strip()
        if ultima_linea=='6':
            resultados.append(True)
        else:
            resultados.append(False)
    return resultados

# esta funcion lee los archivos rollo_proceso y r_revisar
def obtener_rollos(arreglos):
    # indicador = True
    for arreglo in arreglos:
        try:
            list(filter(None,arreglo))[2]
            return True
        except:
            # indicador = False
            return False

#esta funcion lee el archivo l_plano_exp
def leer_plano(archivo):
    if not archivo:
        return  False
    
    indicador = False
    indice = 0
    while not indicador and indice < len(archivo):
        if "KEYSTON BROTHERS" in archivo[indice]:
            indicador = True
        indice += 1

    return indicador


def seguimos(respuestas,rollos,plano):
    validacion = False
    if respuestas and rollos and plano :
        validacion = True
    return validacion
        
        
#aqui se leen los archivos

#archivos de lcantidad_inv_plan y lexis_rollo_plan
print("leyendo lcantidad_lexisrollo_plan")
ruta_rollo_plan ='Z:\\ListadosSeguimientos\CR_lexis_rollo_plan.txt'
print("leyendo lcantidad_inv_plan")
ruta_inv_plan = 'Z:\\ListadosSeguimientos\CR_lcantidad_inv_plan.txt'
  
   
print("leyendo rollo_proceso")

#archivos de rollo_proceso y rollo_revisar
with open('Z:\\ListadosSeguimientos\CR_lrollo_proceso.txt','r',encoding='latin-1') as rollo_proceso:
    ultimalinea_rollo_proceso = rollo_proceso.readlines()[-1]
    arreglo_proceso=re.split(r' ',ultimalinea_rollo_proceso)    
print("leyendo lrollo_revisar")
with open('Z:\\ListadosSeguimientos\CR_lrollo_revisar.txt','r',encoding='latin-1') as rollo_revisar:
    ultimalinea_rollo_revisar = rollo_revisar.readlines()[-1]
    arreglo_revisar=re.split(r' ',ultimalinea_rollo_revisar)
        
#aqui estamos abriendo el archivo L_plano_exp
print("leyendo lpend_plano_exp")
with open('Z:\\ListadosSeguimientos\CR_lpend_plano_exp.txt','r',encoding='latin-1') as Plano_exp:
    archivo_planoexp = Plano_exp.readlines()

#aqui agrupamos las lineas para la funcion leer_Archivo
rutas = [ruta_rollo_plan,ruta_inv_plan]
#esta es la respuesta que nos devulve la funcion leer_archivo
respuestas = leer_archivo(rutas)
print(respuestas)

#aqui declaramos el arreglo para la funcion obtener_rollos
arreglos = [arreglo_proceso, arreglo_revisar]

#esta es la respuesta que nos devuelve
rollos = obtener_rollos(arreglos)
print(rollos)

#esta es la repuesta que nos devuelve la funcion leer_plano ya que la variable se lee apenas se abre el archivo
plano = leer_plano(archivo_planoexp)
print(plano)

grantotal = seguimos(respuestas,rollos,plano)

# print(respuestas)
# print(rollos)
# print(plano)
print(grantotal)    


print("TErminé")