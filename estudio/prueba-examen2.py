import threading
import queue
import time
import random
import math

class Productor(threading.Thread):
    def __init__(self, queue, PT):
        threading.Thread.__init__(self)
        self.queue = queue
        self.PT = PT

    def run(self):
        while True:
            # Genera 10 números aleatorios entre 11 y 999
            for _ in range(10):
                self.queue.put(random.randint(11, 999))
            time.sleep(self.PT)

class Consumidor(threading.Thread):
    def __init__(self, queue, X, CT):
        threading.Thread.__init__(self)
        self.queue = queue
        self.X = X
        self.CT = CT

    def calcular_mcd(self, numeros):
        # Función para calcular el MCD de una lista de números
        def calcular_mcd_de_dos(a, b):
            while b:
                a, b = b, a % b
            return a

        # Calcular MCD de la lista de números
        mcd = numeros[0]
        for num in numeros[1:]:
            mcd = calcular_mcd_de_dos(mcd, num)
        return mcd

    def run(self):
        while True:
            lista_numeros = []
            for _ in range(self.X):
                lista_numeros.append(self.queue.get())
            print(f"Consumiendo: {lista_numeros}")

            # Calcular el MCD de la lista de números
            mcd = self.calcular_mcd(lista_numeros)
            print(f"MCD de {lista_numeros}: {mcd}")
            time.sleep(self.CT)

# Caso 1: 1 Productor, 1 Consumidor con PT=1, CT=4 y X=3
q_1_1 = queue.Queue()
p_1_1 = Productor(q_1_1, PT=1)
c_1_1 = Consumidor(q_1_1, X=3, CT=4)

# Caso 2: 4 Productores, 2 Consumidores con PT=2, CT=4 y X=2
q_4_2 = queue.Queue()
p_4_2 = Productor(q_4_2, PT=2)
c_4_2 = Consumidor(q_4_2, X=2, CT=4)

# Caso 3: 2 Productores, 10 Consumidores con PT=1, CT=10 y X=4
q_2_10 = queue.Queue()
p_2_10 = Productor(q_2_10, PT=1)
c_2_10 = Consumidor(q_2_10, X=4, CT=10)

# Iniciar hilos
p_1_1.start()
time.sleep(1)
c_1_1.start()

p_4_2.start()
time.sleep(1)
c_4_2.start()

p_2_10.start()
time.sleep(1)
c_2_10.start()

# Esperar a que todos los hilos terminen
p_1_1.join()
c_1_1.join()

p_4_2.join()
c_4_2.join()

p_2_10.join()
c_2_10.join()
