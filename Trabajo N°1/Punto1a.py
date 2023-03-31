import csv

# Abrir el archivo CSV en modo de lectura y escritura
with open('Trabajo N°1/tabla_temperaturas.csv', 'r+', newline='') as tabla_temperaturas:
    # Leer el archivo CSV con el módulo csv
    csv_reader = csv.reader(tabla_temperaturas)
    
    # Obtener los encabezados de las columnas
    encabezados = next(csv_reader)

    # Agregar "promedio" como el encabezado de la tercera columna
    encabezados.append("promedio")

    # Crear una lista vacía para almacenar las filas actualizadas
    filas_actualizadas = []

    # Iterar sobre cada fila del archivo CSV
    for fila in csv_reader:
        # Convertir los valores de las primeras dos columnas a números y calcular el promedio
        Promedio = (float(fila[1]) + float(fila[2])) / 2

        # Agregar el promedio como un tercer valor en la fila
        fila.append(Promedio)

        # Agregar la fila actualizada a la lista de filas actualizadas
        filas_actualizadas.append(fila)

    # Escribir las filas actualizadas en un nuevo archivo CSV
    with open('Trabajo N°1/promedios.csv', 'w', newline='') as tabla_actualizada:
        # Escribir los encabezados de las columnas en el archivo actualizado
        csv_writer = csv.writer(tabla_actualizada)
        csv_writer.writerow(encabezados)

        # Escribir las filas actualizadas en el archivo actualizado
        csv_writer.writerows(filas_actualizadas)