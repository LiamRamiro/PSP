import threading
import random
import time

# Lista compartida
shared_list = []

# Lock para acceso a la lista
list_lock = threading.Lock()

# Variable para controlar la suma de la lista
sum_exceeded = False

def generate_numbers():
    global sum_exceeded
    while not sum_exceeded:
        number = random.randint(1, 100)
        with list_lock:
            shared_list.append(number)
        time.sleep(0.1)  # Simula la generación de números a intervalos

def replace_numbers():
    global sum_exceeded
    while not sum_exceeded:
        with list_lock:
            for i in range(len(shared_list)):
                if shared_list[i] % 10 == 0:
                    shared_list[i] = -1
        time.sleep(0.2)  # Simula el recorrido y reemplazo a intervalos

def check_sum():
    global sum_exceeded
    while sum(shared_list) <= 20000:
        time.sleep(1)  # Espera un segundo antes de verificar nuevamente
    sum_exceeded = True
    print("Sum exceeded 20000. Aborting threads.")

def main():
    # Crear hilos
    generate_thread = threading.Thread(target=generate_numbers)
    replace_thread = threading.Thread(target=replace_numbers)
    check_sum_thread = threading.Thread(target=check_sum)

    # Iniciar hilos
    generate_thread.start()
    replace_thread.start()
    check_sum_thread.start()

    # Esperar a que el hilo de comprobación termine
    check_sum_thread.join()

    # Imprimir la lista resultante
    print("Final List:", shared_list)

if __name__ == "__main__":
    main()