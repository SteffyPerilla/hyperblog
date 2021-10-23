
def raiz ():
    opcion = int(input("Cual metodo deseas utilizar para encontrar la raiz de un número: 1 = Aproximación, 2 = busqueda Binaria y 3 = enumeración "))
    if opcion == 1:
        objetivo = int(input('Escoge un numero: '))
        aproximacion(objetivo)
    elif opcion == 2:
        objetivo = int(input('Escoge un numero: '))
        busquedabinaria(objetivo)
    elif opcion == 3:
        objetivo = int(input('Escoge un numero: '))
        enumeracion(objetivo)
    else:
        print('Opcion no valida')


def aproximacion (objetivo):
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontro la razi cuadrada {objetivo}')
    else:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')

def busquedabinaria (objetivo):
    epsilon = 0.01
    bajo = 0.0 
    alto = max(1.0,objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo) / 2

    print(f'La raiz cuadrada de {objetivo} es {respuesta}')

def enumeracion (objetivo):
    respuesta = 0

    while respuesta**2 < objetivo:
        respuesta += 1

    if respuesta**2 == objetivo:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene raiz cuadrada exacta') 

raiz()