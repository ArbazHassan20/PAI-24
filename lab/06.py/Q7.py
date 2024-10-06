import pandas as pd
df = pd.read_excel("employee.xlsx")
specified_year = 2021
if 'Year' in df.columns:
    filtered_df = df[df['Year'] == specified_year]
elif 'Hire Date' in df.columns:
    df['Hire Year'] = pd.to_datetime(df['Hire Date']).dt.year
    filtered_df = df[df['Hire Year'] == specified_year]
else:
    print("No 'Year' or 'Hire Date' column found in the dataset.")
    filtered_df = pd.DataFrame()
print(f"List of employees for the year {specified_year}:")
print(filtered_df)
