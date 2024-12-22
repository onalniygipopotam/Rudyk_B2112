 #1.1
''' from random import randint
lst = [randint(-10,10) for i in range(20)]
print(lst)
sum_negative = 0
for num in lst:
    if num < 0: sum_negative += num
    print("Sum negative item list: ", sum_negative)'''


#1.2
'''import random
numbers = [random.randint(-100, 100) for _ in range(20)]  # Випадковий список
even_sum = sum(num for num in numbers if num % 2 == 0)

print(even_sum)'''


#1.3
''' import random
numbers = [random.randint(-100, 100) for _ in range(20)]
odd_sum = sum(num for num in numbers if num % 2 != 0)
print(odd_sum) '''


#1.4
''' import random
from math import prod
numbers = [random.randint(-100, 100) for _ in range(20)]  
product_indices = prod(numbers[i] for i in range(len(numbers)) if i % 3 == 0)
print("Добуток елементів з індексами кратними 3:", product_indices) '''


#1.5
''' import random
from math import prod
numbers = [random.randint(-100, 100) for _ in range(20)]
min_index = numbers.index(min(numbers))
max_index = numbers.index(max(numbers))
if min_index > max_index:
    min_index, max_index = max_index, min_index
product_between = prod(numbers[min_index + 1:max_index])
print("Добуток елементів між мінімальним і максимальним елементом:", product_between) '''


#1.6
import random
numbers = [random.randint(-100, 100) for _ in range(20)]
positive_indices = [i for i, num in enumerate(numbers) if num > 0]
if len(positive_indices) >= 2:
    first_pos = positive_indices[0]
    last_pos = positive_indices[-1]
    sum_between = sum(numbers[first_pos + 1:last_pos])
else:
    sum_between = 0
print("Сума елементів між першим і останнім додатними елементами:", sum_between)
