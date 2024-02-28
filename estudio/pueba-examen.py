import os
import threading

def count_vowels(file_path, lock, result_dict):
    vowels = "aeiouAEIOU"
    file_stats = os.stat(file_path)
    file_size_mb = file_stats.st_size / (1024 * 1024)

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        vowel_count = sum(1 for char in content if char in vowels)

    with lock:
        result_dict[file_path] = {'File Size (MB)': file_size_mb, 'Vowel Count': vowel_count}

def process_files_in_directory(directory_path, num_threads):
    result_dict = {}
    lock = threading.Lock()
    threads = []

    files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

    for file_name in files:
        file_path = os.path.join(directory_path, file_name)
        thread = threading.Thread(target=count_vowels, args=(file_path, lock, result_dict))
        threads.append(thread)

    # Start the threads
    for thread in threads:
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    return result_dict

if __name__ == "__main__":
    directory_path = input("Enter the directory path (press Enter for the current directory): ") or '.'
    num_threads = int(input("Enter the number of threads to use: "))

    result = process_files_in_directory(directory_path, num_threads)

    # Print the result dictionary
    print("\nResults:")
    for file_name, data in result.items():
        print(f"{file_name}: {data}")

