import os
import time
import todo  # Asegúrate de que este módulo esté correctamente instalado o accesible

# Función para correr el archivo .bat y verificar los archivos
def correr_Bat():
    intentos_maximos = 3
    intentos = 0
    
    while intentos < intentos_maximos:
        print("Iniciando validación")
        
        try:
            # Actualizar archivos_validos en cada intento
            respuestas = todo.leer_archivo(todo.rutas)
            rollos = todo.obtener_rollos(todo.rollos)
            plano = todo.leer_plano(todo.archivo)
            
            # 'seguimos' retorna un booleano
            archivos_validos = todo.seguimos(respuestas, rollos, plano)
            print(f"Valor devuelto por 'seguimos': {archivos_validos} (Tipo: {type(archivos_validos)})")
            
        except Exception as e:
            print(f"Error al procesar los archivos: {e}")
            return False
        
        # Validar si los archivos son válidos
        if archivos_validos:  # Si es True, termina el ciclo
            print("Archivos válidos.")
            return True
        else:  # Si es False, corre el archivo .bat
            print(f"Archivos no válidos, corriendo .bat. Intento número {intentos + 1}")
            try:
                # Ejecuta el archivo VBS
                os.system("Z:\\00_Listados_automaticos\Ejecutables_Listados\ListadosDiarios\SeguimientoCR.vbs")
            except Exception as e:
                print(f"Error al ejecutar el archivo VBS: {e}")
                return False
            
            # Esperar 7 minutos para que los archivos se descarguen o generen
            print("Esperando 7 minutos mientras se descargan los archivos para volver a validar.")
            time.sleep(420)
            
            # Incrementar el contador de intentos
            intentos += 1
            print(f"Revisando nuevamente después del intento número {intentos}")
    
    # Si se agotaron los intentos
    print("Se agotaron los intentos.")
    return False

# Ejecutar la función y mostrar el resultado
if __name__ == "__main__":
    resultado = correr_Bat()
    print("Resultado de la validación:", resultado)
