import pandas as pd

my_data = {
    'title': ['Movie A', 'Movie B', 'Movie C', 'Movie D'],
    'runtime (hrs)': [2.5, 1.5, 3.0, 0.5]  # Runtime in hours
}

df = pd.DataFrame(data=my_data)

# Sorting the DataFrame by 'runtime (hrs)' in ascending order
df = df.sort_values(by='runtime (hrs)', ascending=True)

print(df)
