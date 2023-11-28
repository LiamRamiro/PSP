import threading
import os
import subprocess
import tempfile
import time

file_name = os.path.join(tempfile.gettempdir(), os.urandom(24).hex())

def code(name):
    time.sleep(10)
    data_to_write = f"codigo limpio fue escrito por {name}\n"

    with file_lock:
        with open(file_name, 'a') as f:
            print(f"Guardando en {file_name}")
            f.write(data_to_write)
    subprocess.run(["ping", "google.com"])


