numbers_str = '4 8 6 2 1 2 3 4 4 0 2 4 4 5 8 2 9 6 0 0'
numbers = list(numbers_str)
def get_unicum(numbers):
    unicue = []
    for number in numbers:
        if number in unicue:
            continue
        else:
            if number != ' ': unicue.append(number)
    return ' '.join(unicue)
print(get_unicum(numbers))
