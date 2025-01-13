first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(_) for _ in first_strings if len(_) >= 5]
second_result = [(s1, s2) for s1 in first_strings for s2 in second_strings if len(s1) == len(s2)]
third_result = {s: len(s) for s in first_strings + second_strings if len(s)%2==0}

print(first_result)
print(second_result)
print(third_result)
