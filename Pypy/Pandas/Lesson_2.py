# File - Pandas
import pandas as pd

# CSV
df = pd.read_csv("data.csv")   # Hãy tạo file.csv

print(df)                   # Chỉ trả về 5 dòng đầu và 5 dòng cuối
print(df.to_string())       # Trả về đầy đủ bao gồm cả dòng

print(pd.options.display.max_rows)
pd.options.display.max_rows = 9999

# JSON
df2 = pd.read_json("data.json")   # Hãy tạo file.json

print(df2.to_string())

print(df.head())            # In ra 5 dòng đầu tiên từ trên xuống dưới
print(df.tail())            # In ra 5 dòng cuối cùng từ dưới lên trên
print(df.info())            # In ra thông tin đầy đủ

print(df.iloc[0:15:2, 0:3])   # Hàng và cột trong "iloc"

# CONDITION - WHERE
print(df[df["Calories"] > 500])
print(df[(df["Duration"] >= 45) & (df["Calories"] > 400)])
print(df[(df["Pulse"] > 110) & (df["Maxpulse"] < 150)])
print(df[(df["Duration"] < 30) | (df["Calories"] > 300)].to_string())

print(df[(df["Pulse"] > 130) & (df["Maxpulse"] > 170)])
print(df[(df["Pulse"] < 100) & (df["Calories"] < 250)])
print(df[(df["Duration"] > 60) | (df["Calories"] < 300)])

print(df.sum())
print(df.mean())
print(df.count())
print(df.max())
print(df.min())
print(df['Duration'].sum())

group = df.groupby("Duration")
print(group["Pulse"].mean(), 2)
print(group["Pulse"].sum())
print(group["Pulse"].min())
print(group["Pulse"].max())
print(group["Pulse"].count())