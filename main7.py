# Напишите функцию, принимающую на вход строку и символ и возвращает количество вхождений символа в строку или
# её длину если строка символ не содержит
import sys


# Sample Input:
# ц
# Величайший урок жизни в том, что и дураки бывают правы.( Уинстон Черчилль )

# Sample Output:

# 75

def strWork(strInput, symInput):
    nums = strInput.count(symInput)
    if nums > 0:
        return nums
    else:
        return len(strInput)


#lines = sys.stdin.readlines()
#print()
#lines = [line for line in sys.stdin]

#five_lines = list(itertools.islice(sys.stdin, 5))

strInput = 'Величайший урок жизни в том, что и дураки бывают правы.( Уинстон Черчилль )'
strInput = strInput.lower()
symInput = 'ц'
print(strWork(strInput, symInput))
