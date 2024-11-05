import re


with open('Z:\\ListadosSeguimientos\CR_lpend_plano_exp.txt','r',encoding='latin-1') as rollo_proceso:
    archivo = rollo_proceso.readlines()

print(archivo)

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

plano = leer_plano(archivo)

print(plano)



    

       
    
    


        
    