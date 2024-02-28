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
            num = random.randint(101, 499)
            self.queue.put(num)
            print(f"Produciendo: {num}")
            time.sleep(self.PT)

class Consumidor(threading.Thread):
    def __init__(self, queue, X, CT):
        threading.Thread.__init__(self)
        self.queue = queue
        self.X = X
        self.CT = CT

    def run(self):
        while True:
            nums = []
            for i in range(self.X):
                num = self.queue.get()
                nums.append(num)
                print(f"Consumiendo: {num}")

            multiplicacion = 1
            for num in nums:
                multiplicacion *= num

            print(f"Consumidos: {nums}, Multiplicación: {multiplicacion}")
            time.sleep(self.CT)

q_1_1 = queue.Queue()
p_1_1 = Productor(q_1_1, PT=1)
c_1_1 = Consumidor(q_1_1, X=3, CT=4)


q_4_2 = queue.Queue()
p_4_2 = Productor(q_4_2, PT=2)
c_4_2 = Consumidor(q_4_2, X=2, CT=2)


q_2_6 = queue.Queue()
p_2_6 = Productor(q_2_6, PT=1)
c_2_6 = Consumidor(q_2_6, X=4, CT=10)


p_1_1.start()
time.sleep(1)
c_1_1.start()

p_4_2.start()
time.sleep(1)
c_4_2.start()

p_2_6.start()
time.sleep(1)
c_2_6.start()

p_1_1.join()
c_1_1.join()

p_4_2.join()
c_4_2.join()

p_2_6.join()
c_2_6.join()
