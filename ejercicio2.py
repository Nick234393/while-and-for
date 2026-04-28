#piramide
piramide_numerica = ""
numero_positivo = int(input("Ingrese numero entero positivo: "))
while numero_positivo < 0:
    print("Error ingrese otro numero")
    numero_positivo = int(input("Ingrese numero entero positivo: "))

for numero_positivo in range(1,numero_positivo,2):
    piramide_numerica = str(numero_positivo) + "" +piramide_numerica
    print(piramide_numerica)
