import random
from math import prod

numbers = [random.randint(-100, 100) for _ in range(20)]
print("Список чисел:", numbers)

negative_sum = sum(num for num in numbers if num < 0)
print("Сума від'ємних чисел:", negative_sum)

even_sum = sum(num for num in numbers if num % 2 == 0)
print("Сума парних чисел:", even_sum)

odd_sum = sum(num for num in numbers if num % 2 != 0)
print("Сума непарних чисел:", odd_sum)

product_indices = prod(numbers[i] for i in range(len(numbers)) if i % 3 == 0)
print("Добуток елементів з індексами кратними 3:", product_indices)

min_index = numbers.index(min(numbers))
max_index = numbers.index(max(numbers))
if min_index > max_index:
    min_index, max_index = max_index, min_index
product_between = prod(numbers[min_index + 1:max_index])
print("Добуток елементів між мінімальним і максимальним елементом:", product_between)

positive_indices = [i for i, num in enumerate(numbers) if num > 0]
if len(positive_indices) >= 2:
    first_pos = positive_indices[0]
    last_pos = positive_indices[-1]
    sum_between = sum(numbers[first_pos + 1:last_pos])
else:
    sum_between = 0
print("Сума елементів між першим і останнім додатними елементами:", sum_between)
