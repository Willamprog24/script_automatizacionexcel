import os

ruta_rollo_plan ='Z:\\ListadosSeguimientos\CR_lexis_rollo_plan.txt'
ruta_inv_plan = 'Z:\\ListadosSeguimientos\CR_lcantidad_inv_plan.txt'

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

# Rollo_plan = leer_archivo(ruta_rollo_plan)
# rollo_inv_plan = leer_archivo(rutal_inv_plan)

rutas = [ruta_inv_plan,ruta_rollo_plan]



todo=leer_archivo(rutas)
print(todo)


