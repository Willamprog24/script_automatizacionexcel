import re



ruta_plano_exp='Z:\\ListadosSeguimientos\CR_lpend_plano_exp.txt'

# with open('Z:\\ListadosSeguimientos\CR_lpend_plano_exp.txt','r',encoding='latin-1') as rollo_proceso:
#      archivo = rollo_proceso.readlines()

def leer_plano(ruta):
    with open(ruta,'r',encoding='latin-1') as plano_exp: 
        archivo = plano_exp.readlines()
    indicador = False
    indice = 0
    
    while indicador == False:
        if "KEYSTON BROTHERS" in archivo[indice]:
            indicador = True
        indice = indice + 1
    return indicador

plano = leer_plano(ruta_plano_exp)

print(plano)