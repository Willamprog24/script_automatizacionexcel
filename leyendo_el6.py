import re

def leer_archivo(ultima_linea):
    respuestas = []
    for i, linea in enumerate(ultima_linea):
        if linea =='6':
            respuestas.append(True)
        else:
            respuestas.append(False)
    return respuestas


with open('Z:\\ListadosSeguimientos\CR_lcantidad_inv_plan.txt','r',encoding='latin-1') as inv_plan:
   ultima_linea_inv = inv_plan.readlines()[-1]
   
with open('Z:\\ListadosSeguimientos\CR_lexis_rollo_plan.txt','r',encoding='latin-1') as lexis_rollo:
   ultima_linea_lexis = lexis_rollo.readlines()[-1]

conjunto_lineas = [ultima_linea_inv, ultima_linea_lexis]


respuestas = leer_archivo(conjunto_lineas)


print(respuestas) 

        
