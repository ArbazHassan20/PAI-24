import pandas as pd
Data = ["key 1", "key 2", "key 3"]
df = pd.DataFrame(Data)
new_index = range(100, 100 + len(df))
df.index = new_index
print(df)
