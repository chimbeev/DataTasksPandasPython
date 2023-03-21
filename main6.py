# Вычислите среднее значение столбца 'grade'

# Sample Input:

# stud_id; Subject; grade
# 1;ТВиМС;60
# 2;МОР;70
# 3;ТВиМС;80
# 4;МОР;85
# 5;ТВиМС;100
# Sample Output:

# 79
import sys, io

import pandas as pd
# Записываем в input() или sys.stdin
sys.stdin = io.StringIO('stud_id;Subject;grade\n1;ТВиМС;60\n2;МОР;70\n3;ТВиМС;80\n4;МОР;85\n5;ТВиМС;100\n')
# Читаем из input() или sys.stdin
inp = sys.stdin.read()
# Создаем датафрейм из input()
data = pd.read_csv(io.StringIO(inp), sep=';')
# print(data)
# Вычисляем среднее значение столбца
# print(data['grade'].mean())
# print(data.grade.max() - data.grade.min())
# print(data[data.Subject == 'ТВиМС'])
# print(data.info())
df1 = data[[data.grade < 85] and [data.grade > 60]]
print(df1)

