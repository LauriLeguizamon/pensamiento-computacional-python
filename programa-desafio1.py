print('Este es un programa para aproximar la raiz cuadrada de casi cualquier numero y puedes elegir con que algoritmo hacerlo!!')
objetivo = int(input('Escoje un numero: '))
print('''
Tienes las siguientes opciones de algoritmos:
 1 Enumeracion exaustiva
 2 Busqueda binaria
''')
algoritmo = int(input('Escoge que algoritmo quieres escribiendo su correspondiente numero: '))
epsilon = float(input('Tambien nos ayudaria si nos dijeras con que margen de error quieres trabajar (por ejemplo 0,1): '))

def enumeracion_exaustiva():
    paso = epsilon**2
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        respuesta += paso

    if abs(respuesta ** 2 - objetivo) >= epsilon:
        print(f'No se encontro la raiz cuadrada de { objetivo }')
    else: 
        print(f'La raiz cuadrada de { objetivo } es { respuesta }')

def busqueda_binaria():
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo) / 2

    print(f'La raiz cuadrada de { objetivo } es { respuesta }')

if algoritmo == 1:
    enumeracion_exaustiva()
else:
    busqueda_binaria()

