
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(i) for i in first_strings if len(i) > 5]
second_result = [(x, y) for x in second_strings for y in first_strings if len(y) == len(x)]
third_result = {f'{i}': len(i) for i in [*first_strings, *second_strings] if len(i) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)
