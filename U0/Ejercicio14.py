class opciones:
    def __init__(self):
        print("Te voy a dar tres opciones para que elijas")
        print("     1. Volcado(escritura) de una lista con todos los número pares comprendidos entre 0 y 100")
        print("     2. Mostrar (lectura) del fichero de texto creado en la opción 1")
        print("     3. Salir del programa")
        opcion = int(input("¿Qué opción eliges?"))
        while opcion != 3:
            if opcion == 1:
                self.volcar()
            elif opcion == 2:
                self.mostrar()
            else:
                print("Opción no válida")
            opcion = int(input("¿Qué opción eliges?"))
        print("Adiós")

    def volcar(self):
        with open('parificador.txt', 'w') as archivo:
            for i in range(0, 101, 2):
                archivo.write(str(i) + ' ')
                if i % 10 == 0 and i > 0:
                    archivo.write('\n')
        archivo.close()
        print("Volcado realizado")

    def mostrar(self):
        archivo = open('parificador.txt', 'r')
        mensaje = archivo.read()
        print(mensaje)
        archivo.close()
        print("Lectura realizada")


opciones()  