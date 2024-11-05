import todo 
import os
import time



def correr_bat():
    intentos = 0  # Inicializamos el contador de intentos
    maximo = 3  # Número máximo de intentos

    while intentos < maximo:
        
        archivo=todo.archivo_planoexp
        # Leer los archivos en cada intento para que se actualicen
        respuestas = todo.leer_archivo(todo.rutas)
        rollos = todo.obtener_rollos(todo.arreglos)
        plano = todo.leer_plano(archivo)

        print(respuestas)
        print(rollos)
        print(plano)
        
        # Validación de archivos en cada intento
        archivo = todo.seguimos(respuestas,rollos,plano)

        if archivo:  # Si los archivos son válidos
            print("Archivos válidos")
            break  # Salimos del bucle
        else:
            print(f"Archivos no válidos, corriendo .bat. Intento número {intentos + 1}")
            os.system("Z:\\00_Listados_automaticos\\Ejecutables_Listados\\ListadosDiarios\\SeguimientoCR.vbs")

            # Esperar 7 minutos para que los archivos se descarguen o generen
            print("Esperando 7 minutos mientras se descargan los archivos para volver a validar.")
            time.sleep(420)
            
            intentos += 1  # Incrementar el contador de intentos

    if intentos == maximo:
        print("Se agotaron los intentos y los archivos siguen siendo inválidos.")
    else:
        print("La validación se completó con éxito.")

# Llamada a la función
correr_bat()
