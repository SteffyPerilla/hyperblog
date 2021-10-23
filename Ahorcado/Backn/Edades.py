nombre_1=input("Cual es tu nombre: ")
Edad_1 = int(input(nombre_1 + " Cual es tu edad: "))
nombre_2=input("Cual es tu nombre: ")
Edad_2=int(input( nombre_2 + " Cual es tu edad "))

if Edad_1 < Edad_2:
    print(nombre_1 + " es menor que " + nombre_2)
elif Edad_1 > Edad_2:
    print(nombre_1 + " es mayor que " + nombre_2)
else:
    print(nombre_1 + " y " + nombre_2 + " tienen la misma edad ")