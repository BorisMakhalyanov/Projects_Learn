def apply_all_func(int_list, *functions):
    # В функции apply_all_func создайте пустой словарь reuslts.
    results = {}
    # Переберите все функции из *functions.
    for func in functions:
        try:
            # Функция apply_all_func(int_list, *functions) должна:
            # Вызвать каждую функцию к переданному списку int_list
            # При переборе функций записывайте в словарь reuslts результат работы этой функции под ключом её названия.
            results[func.__name__] = func(int_list) #возврат словаря
        except Exception as e:
            # Исключение возникнет, если функция не предназначена для работы с переданным типом данных.
            results[func.__name__] = str(e)
    # Функция apply_all_func(int_list, *functions) должна:
    # Возвращать словарь, где ключом будет название вызванной функции, а значением -
    # её результат работы со списком int_list.
    return results


print(apply_all_func([6, 20, 15, 9], max, min))

print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
