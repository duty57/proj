import pandas as pd

df = pd.read_csv('archive/population.csv')

df['PopTotal'] = df['PopTotal'].apply(lambda x: x.replace(',', '.'))
df['PopTotal'] = df['PopTotal'].astype('float32')

group_df = df.groupby('Location')

print(group_df['PopTotal'].mean())