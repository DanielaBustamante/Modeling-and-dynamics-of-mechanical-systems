import csv

with open('Tabla_temperaturas.csv', 'r') as archivo:
    lector_csv = csv.reader(Tabla_temperaturas)
    for fila in lector_csv:
        print(fila)
        
