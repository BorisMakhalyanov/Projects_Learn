def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for element in numbers:
        try:
            result += element
        except TypeError:
            incorrect_data += 1
    return result, incorrect_data

def calculate_average(numbers, silence=True):
    try:
        sum, incorrect = personal_sum(numbers)
        if not silence:
            print(f'> аргумент = "{numbers}", сумма = {sum}, некорректные = {incorrect}')
        result = sum / (len(numbers) - incorrect)
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных!')
        return
    return result

def main():
    print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
    print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
    print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
    print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать'''

if __name__ == '__main__':
    main()
