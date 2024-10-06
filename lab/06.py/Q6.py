import pandas as pd
df = pd.read_csv("world_alcohol_consumption.csv")
filtered_df = df[df['Year'].isin([1987, 1989])]
print(filtered_df)
