numero = input("Ingrese numero: ")
try:
    ival = float(numero)
except:
    print("[ERROR]: No es un numero xd")

nvalido = True
while nvalido == True:
    try:
        num = int(input("Ingrese un numero: "))
        if num >= 0 and num <= 10:
            nvalido= False
        else:
            print("Numero fuera de rango ")
        
    except:
        print("ERROR el tipo de dato ingresado no es valido ")

print("El numero ", num , "Es valido")
