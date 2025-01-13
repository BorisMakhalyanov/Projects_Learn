first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(s1)-len(s2) for s1, s2 in zip(first, second) if len(s1) != len(s2))
second_result = (len(first[k])==len(second[k]) for k in range(len(first or second))) # здесь не важно какой список
                                                                                    # использовать второй или первый

print(list(first_result))
print(list(second_result))
