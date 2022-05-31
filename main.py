import pandas as pd

df = pd.read_csv('archive/population.csv', index_col='Location')

df['PopTotal'] = df['PopTotal'].apply(lambda x: x.replace(',', '.'))
df['PopTotal'] = df['PopTotal'].astype('float32')

group_df = df.groupby('Location')

it_pop = df.loc['Italy', 'PopTotal']
years = df['Time'].head(20)
print(it_pop)
# print(group_df['PopTotal'].mean())
# print(df[df['Location'] == 'Africa'])