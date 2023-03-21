import pandas as pd

lst = list(map(int, '7 11 3 5 10 12 11 9 6 1 8 11 1 4 9'.split()))

df = pd.DataFrame(lst)

print(df.median())

print(df.var())

lst_x = list(map(int, '2 10 5 4 7 7 1 4 7 8 6 6 6 7 10'.split()))
lst_y = list(map(int, '3 4 7 11 2 11 11 8 8 1 2 2 8 5 9'.split()))
x = pd.Series(lst_x)
y = pd.Series(lst_y)
print(round(x.cov(y), 1))


