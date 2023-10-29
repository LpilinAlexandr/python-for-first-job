"""
Понимание асимптотической сложности в базовых операциях
https://wiki.python.org/moin/TimeComplexity
https://leetcode.com/
"""

# Хотя бы самая минимальная база по Big O notation.

# Чем отличается поиск в списке
if 100500 in [1, 2, 3]:
    ...

# от поиска в множестве
if 100500 in {1, 2, 3}:
    ...


new_test_list = []

# В чем разница между:
for item in (1, 2, 3):
    new_test_list.append(item)
    # vs
    new_test_list.insert(0, item)


# Какая сложность у
new_test_list.pop(-1)
# и у
number = new_test_list[4]


new_list = [1, 2, 3, ]
# Что лучше. Вот так:
for i in range(3):
    new_list.append(i)

# или
new_list.extend([i for i in range(3)])
