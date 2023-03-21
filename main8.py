# С помощью анонимной lambda-функции создайте столбец "EurGrad", который переводит значения оценок столбца 'grade'
# в европейскую систему.
# Sample Input:
# stud_id;Subject;grade
# 1;ТВиМС;60
# 2;МОР;70
# 3;ТВиМС;80
# 4;МОР;85
# 5;ТВиМС;100
# Sample Output:
# E D C B A

import sys, io
import pandas as pd
# Записываем в input() или sys.stdin
sys.stdin = io.StringIO('stud_id;Subject;grade\n1;ТВиМС;60\n2;МОР;70\n3;ТВиМС;80\n4;МОР;85\n5;ТВиМС;100\n')
# Читаем из input() или sys.stdin
inp = sys.stdin.read()
# Создаем датафрейм из input()
data = pd.read_csv(io.StringIO(inp), sep=';')
# print(data)
data['EurGrad'] = data['grade'].apply(lambda grad: 'E' if 60 <= grad < 65 else 'D' if 65 <= grad < 75
else 'С' if 75 <= grad < 85 else 'B' if 85 <= grad < 90 else 'A' if grad >= 90 else '')
str1 = data['EurGrad'].to_frame().T.to_string(index=False)

print(str1[-10:].replace(' ', ''))






# df1 = data['EurGrad'].to_frame().T
# print(df1.to_string(index=False, ))



