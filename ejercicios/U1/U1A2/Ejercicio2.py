import multiprocessing

def print_cube(num):
    cube = num ** 3
    print(f"The cube of number {num} is {cube}")

def print_square(num):
    square = num ** 2
    print(f"The square of number {num} is {square}")

def main():
    with multiprocessing.Pool(processes=2) as pool:
        numbers = [2, 3, 4, 5, 6]
        pool.starmap(print_square, [(num,) for num in numbers])
        pool.starmap(print_cube, [(num,) for num in numbers])

if __name__ == "__main__":
    main()