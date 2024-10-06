import pandas as pd

my_data = {
    'title': ['Movie A', 'Movie B', 'Movie C', 'Movie D'],
    'revenue': [2.5, 1.5, 3.0, 0.5],  
    'budget': [0.5, 1.2, 0.8, 0.3]   
}

df = pd.DataFrame(data=my_data)


filtered_movies = df[(df['revenue'] > 2) & (df['budget'] < 1)]

print(filtered_movies)
