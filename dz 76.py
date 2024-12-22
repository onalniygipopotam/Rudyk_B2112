first_element = int(input("Введіть перший елемент прогресії: "))
difference = int(input("Введіть різницю прогресії: "))

progression = [first_element + difference * i for i in range(10)]
print("Арифметична прогресія:", progression)
