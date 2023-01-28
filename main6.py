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
sys.stdin = io.StringIO('1;ТВиМС;60\n2;МОР;70\n3;ТВиМС;80\n4;МОР;85\n5;ТВиМС;100\n')

inp = sys.stdin.read()
#print(inp)
#data = pd.read_csv(io.StringIO(inp), sep=';')
#print(data.head())
#print(type(data))
#print(data.columns)
#df = len(data[[' Subject']][' Subject'].unique())
print(inp)