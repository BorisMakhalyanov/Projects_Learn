def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        for div in range(2, result):
            if result % div == 0:
                print(f'Составное')
                return result
        print('Простое')
        return result

    return wrapper

@is_prime
def sum_three(x, y, z):
    return x + y + z

def main():
    result = sum_three(1, 6, 4)
    print(result)

    result = sum_three(3, 5, 6)
    print(result)

if __name__ == '__main__':
    main()