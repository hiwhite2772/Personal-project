import pandas as pd
df = pd.read_csv("data.csv")

new_df = df.dropna()
print(new_df.to_string())

df.dropna(inplace=True)
df.fillna(130, inplace=True)
df.fillna({"Calories":130}, inplace=True)

print(df.to_string())

x = df["Calories"].mean()
df2 = df.fillna({"Calories":x}, inplace=True)
print(df2.to_string())

x2 = df["Calories"].median()
df3 = df.fillna({"Calories":x}, inplace=True)
print(df3.to_string())

df.drop_duplicates(inplace=True)

print(df.to_string())
print(df.duplicated())