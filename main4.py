import pandas as pd
df = pd.read_json('kinopoisk.jsonl', lines = True)
# print(df.info())
# print(df['author'])
# print(len(df['movie_name'].unique()))

# print(df[ df['movie_name'].str.contains('\(1973', case=False) ]['movie_name'].unique())
# print(df.sort_values(by='movie_name').tail(30)['movie_name'],['grade10'])
#print(df['movie_name'])
# print(df[['movie_name', 'grade10']].sort_values('grade10').tail(20))
# print(df[['movie_name', 'grade10']])
print(df.columns)