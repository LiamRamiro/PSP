import threading
import random

# Lista para almacenar los resultados de cada hilo
resultados = []
# Variable para almacenar el hilo ganador
hilo_ganador = None

def sumar_numeros():
    global hilo_ganador
    numeros = [random.randint(1, 1000) for _ in range(100)]
    suma = sum(numeros)
    resultados.append((threading.current_thread().name, suma))
    
    if hilo_ganador is None or suma > resultados[hilo_ganador][1]:
        hilo_ganador = len(resultados) - 1

    print(f'Hilo {threading.current_thread().name}: Resultado = {suma}')

def main():
    # Lista para almacenar los objetos de hilo
    hilos = []

    # Crear 10 hilos
    for i in range(10):
        hilo = threading.Thread(target=sumar_numeros, name=f'Hilo-{i+1}')
        hilos.append(hilo)

    # Iniciar cada hilo
    for hilo in hilos:
        hilo.start()

    # Esperar a que cada hilo termine
    for hilo in hilos:
        hilo.join()

    # Mostrar resultados de cada hilo
    print("\nResultados de cada hilo:")
    for nombre, suma in resultados:
        print(f'{nombre}: {suma}')

    # Mostrar hilo ganador
    print(f'\nEl hilo ganador es {resultados[hilo_ganador][0]} con un resultado de {resultados[hilo_ganador][1]}.')

if __name__ == "__main__":
    main()
