def cambiar_ultimo_primero():
    cadena = input("Introduce una cadena de carácteres y te cambio el primero por el último...")
    print("La cadena con el primero y el último cambiados es",cadena[-1]+cadena[1:-1]+cadena[0])
    print(cadena)
    
cambiar_ultimo_primero()