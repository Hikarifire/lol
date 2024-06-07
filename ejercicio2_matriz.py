def almacenar_datos(p_personas):
    with open("Lista_matriz.csv", "w", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(p_personas)
###################################################
import csv

personas = [["Nombre"," Apellido"]]

for vueltas in range(3):
    nombres = input("Ingrese nombre: ")
    Apellido = input("Escriba apellido: ")
    nombres_apellido = [nombres, Apellido]
    personas.append(personas)




