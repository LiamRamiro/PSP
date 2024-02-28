import threading
import os
import subprocess
import tempfile
import time

file_name = os.path.join(tempfile.gettempdir(), os.urandom(24).hex())

def code(name):
    time.sleep(10)
    with file_lock:
        with open(file_name, 'a') as f:
            print(f"Guardando en {file_name}")
            f.write("codigo limpio fue escrito por "+str(name)) 
        subprocess.run(["ping","-c","4","google.com"])

def multihilo():
    threads = []
    for i in range(4):  
        thread = threading.Thread(target=code, args=(f"Thread-{i+1}",))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    file_lock = threading.Lock()
    multihilo()
