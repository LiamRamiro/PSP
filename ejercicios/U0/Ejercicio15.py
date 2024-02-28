class fichero:   
    def __init__(self):
        print("Te voy a dar tres opciones para que elijas")
        print("     1. Creación(escritura) de un archivo con el texto que me des")
        print("     2. Mostrar (lectura) del fichero de texto creado en la opción 1 con espacios")
        print("     3. Mostrar (lectura) del fichero de texto creado en la opción 1 sin espacios")
        print("     4. Salir del programa")
        opcion = int(input("¿Qué opción eliges?"))
        while opcion != 4:
            if opcion == 1:
                self.volcar()
            elif opcion == 2:
                self.mostrar(True)
            elif opcion == 3:
                self.mostrar(False)
            else:
                print("Opción no válida")
            opcion = int(input("¿Qué opción eliges?"))
        print("Adiós")

    def volcar(self):
        texto = input("¿Qué ponemos?")
        archivo = open('lecturador.txt', 'w')
        archivo.write(texto)
        archivo.close()
        print("Volcado realizado")

    def mostrar(self, espacios):
        archivo = open('lecturador.txt', 'r')
        if not espacios:
            mensaje = archivo.read().replace(' ', '')
        else:
            mensaje = archivo.read()
        print(mensaje)
        archivo.close()
        print("Lectura realizada")


fichero() 