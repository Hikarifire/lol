def nombre_mas_largo(lista):
    for x in range(3):
        if x==0:
            nombre_largo = lista(0)
        else:
            if len(nombre[x]) > len (nombre_largo):
                nombre_largo = lista[x]
    print("El nombre más largo es: ", nombre_largo)
import csv
lista_nombres = []

with open ("nombres_de_la_lista.csv","w", newline="") as archivo:
    escritor = csv.writer(archivo)
    for vuelta in range(3):
        nombre = input("Ingrese nombre: ")
        lista_nombres.append(nombre)
    escritor.writerow(lista_nombres)

nombre_mas_largo(lista_nombres)
