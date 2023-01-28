# Преобразуйте заданный список чисел в список квадратов чисел. Исходный список представляет собой строку,
# результатом работы программа тоже должна быть строка.
# Sample Input:
# -3 -5 3 4 2 -3 8 3 2 -10
# Sample Output:
# 9 25 9 16 4 9 64 9 4 100
def kvadrat(number):
    return number*number


numbers_str = '-3 -5 3 4 2 -3 8 3 2 -10'
numbers = list(numbers_str.split(" ")) # разделили на строки-числа
new_numbers = map(int, numbers) # перевели в число
#print(new_numbers)
numb = list(map(kvadrat, new_numbers))
print("numb", numb)
s = ' '.join(str(x) for x in numb)
print(s)


