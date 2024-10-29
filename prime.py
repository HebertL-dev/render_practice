import math

def is_prime(number):
    """Esta funcion define si el numero es primo o no """
    if number <= 1:
        return False
    #Con este for nos aseguramos de que el numero sea mayor de 2
    for i in range(2, int(math.sqrt(number) + 1)):
        if number % i == 0:
            return False
    return True

def main():
    """Tiene toda la logica principal. """
    for i in range(100):
        if is_prime(i):
            print(i, end=' ')
    print()

if __name__ == '__main__':
    main()
