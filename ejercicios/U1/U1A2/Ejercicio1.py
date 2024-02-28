import multiprocessing
import os

def my_id(task_id):
    process_id = os.getpid()
    print(f"Hi, I'm worker {task_id} (with PID {process_id})")

def main():
    num_cores = multiprocessing.cpu_count()
    pool_size = num_cores - 1

    with multiprocessing.Pool(processes=pool_size) as pool:
        task_ids = list(range(1, 2 * num_cores + 1))
        pool.map(my_id, task_ids)

if __name__ == "__main__":
    main()
