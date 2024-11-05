import xlwings as xw

# Iniciar la aplicación de Excel
app = xw.App()

# Abrir el libro de Excel
WB = xw.books.open('C:\\Listados\\Seguimiento diario 06-05-2024 CR.xlsm')

# Nombres a eliminar
nombres_a_eliminar = ["Criteria", "Extract", "Área_de_extracción", "Criterios"]

try:
    # Recorrer los nombres definidos en el libro
    for nombre in WB.names:
        # Verificar si el nombre debe ser eliminado
        if nombre.name in nombres_a_eliminar:
            # Eliminar el nombre
            nombre.delete()
except Exception as e:
    print(f"Error al eliminar nombres: {e}")

# Guardar cambios en el libro
WB.save()

# Cerrar el libro de Excel
WB.close()

# Cerrar la aplicación de Excel
app.quit()
