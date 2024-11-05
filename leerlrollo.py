import re

def obtener_rollos(arreglo):
    # indicador = True
    for arreglo in arreglos:
        try:
            list(filter(None,arreglo))[2]
            return True
        except:
            # indicador = False
            return False

with open('Z:\\ListadosSeguimientos\CR_lrollo_proceso.txt','r',encoding='latin-1') as rollo_proceso:
    ultimalinea_rollo_proceso = rollo_proceso.readlines()[-1]
    arreglo_proceso=re.split(r' ',ultimalinea_rollo_proceso)    
with open('Z:\\ListadosSeguimientos\CR_lrollo_revisar.txt','r',encoding='latin-1') as rollo_revisar:
    ultimalinea_rollo_revisar = rollo_revisar.readlines()[-1]
    arreglo_revisar=re.split(r' ',ultimalinea_rollo_revisar)    

arreglos = [arreglo_proceso, arreglo_revisar]


rollos = obtener_rollos(arreglos)



arreglo1leido=obtener_rollos(arreglo_proceso)
arreglo2leido=obtener_rollos(arreglo_revisar)
print(arreglo1leido,arreglo2leido)

print(rollos)