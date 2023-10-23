def cantidad_ceros():    
    numeros = []
    for i in range(10):
        numeros.append(int(input("Dime un número...")))
    print(numeros)
    numeros_mayores_0 = [num for num in numeros if num > 0]
    numeros_menores_0 = [num for num in numeros if num < 0]
    print('La cantidad de veces que se ha introducido el 0 es: ', numeros.count(0))
    print('La cantidad de veces que se ha introducido un número mayor de 0 es: ', len(numeros_mayores_0))
    print('La cantidad de veces que se ha introducido un número menor de 0 es: ', len(numeros_menores_0))

cantidad_ceros()