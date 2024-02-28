import multiprocessing
import time
import subprocess
import os

def p1():
    subprocess.run(["cmd.exe"])

def p2():
    time.sleep(5)
    print("Cambiando la prioridad de cmd.exe...")
    current_process = os.nice(10)

def p3(parent_pid):
    time.sleep(7)
    print("Matando a cmd.exe...")
    try:
        os.kill(parent_pid, 9)
    except OSError:
        pass

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=p1)
    p1.start()

    p2 = multiprocessing.Process(target=p2)
    p2.start()

    time.sleep(2)  

    p3 = multiprocessing.Process(target=p3, args=(p1.pid,))
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    print("Programa terminado correctamente.")

    

