def juego():
    from random import randint
    aleatorio = randint(0,20)
    acierto = False
    intentos = 0
    while not acierto:
        respuesta = int(input("¿Qué numero he pensado?"))
        intentos += 1
        if int(respuesta) == aleatorio:
            print("Enhorabuena, has acertado en el intento:", intentos, "el número que había pensado es", aleatorio)
            acierto = True
        else:
            #print(aleatorio)#para comprobar que no cambia el número pensado
            if respuesta < aleatorio:
                print(respuesta, "es menor, llevas",intentos,"intento(s)")
            else:
                print(respuesta, "es mayor, llevas",intentos,"intento(s)")
            

juego()