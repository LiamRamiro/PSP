import threading
import queue
import time
import random

class Productor(threading.Thread):
    def __init__(self, queue, PT):
        threading.Thread.__init__(self)
        self.queue = queue
        self.PT = PT
    def run(self):
        while True:
            for _ in range(15):
                self.queue.put(random.randint(50, 2000))
            time.sleep(self.PT)

class Consumidor(threading.Thread):
    def __init__(self, queue, X, CT):
        threading.Thread.__init__(self)
        self.queue = queue
        self.X = X
        self.CT = CT

    def run(self):
        while True:
            list = []  
            for i in range(self.X):
                list.append(self.queue.get())
                print(f"Consumiendo: {list[i]}")

            suma_cuadrados = sum([x**2 for x in list])
            print(f"Consumidos: {list}, Suma de cuadrados: {suma_cuadrados}")
            time.sleep(self.CT)


q_1_1 = queue.Queue()
p_1_1 = Productor(q_1_1, PT = 2)
c_1_1 = Consumidor(q_1_1, X = 4, CT=6)

q_5_2 = queue.Queue()
p_5_2 = Productor(q_5_2, PT = 1)
c_5_2 = Consumidor(q_5_2, X = 5, CT=3)

q_3_10 = queue.Queue()
p_3_10 = Productor(q_3_10, PT = 3)
c_3_10 = Consumidor(q_3_10, X = 2, CT=8)


p_1_1.start()
time.sleep(1)
c_1_1.start()

p_5_2.start()
time.sleep(1)
c_5_2.start()

p_3_10.start()
time.sleep(1)
c_3_10.start()

p_1_1.join()
c_1_1.join()


p_5_2.join()
c_5_2.join()

p_3_10.join()
c_3_10.join()



