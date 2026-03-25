import pandas as pd
data = {
    "name" : ["An", "Binh", "Chi", "Dung", "Em"],
    "age": [20, 21, 22, 23, 20],
    "class" : ["A", "A", "B", "B", "A"],
    "score" : [8, 9, 7, 10, 6]
}

df = pd.DataFrame(data)

print(df)
print()

print(df.head(3))  #In 3 dòng phần tử đầu tiên
print()

print(df.tail(3))  #In 3 dòng phần tử cuối cùng
print()

print(df[df["score"] > 7])  #In kết quả hơn điểm 7 trở lên
print()

print(df["score"].mean())  #Tổng điểm trung bình
print()

print(round(df.groupby("class")["score"].mean(), 2))  #Nhóm lớp riêng theo tổng điểm trung bình 
print()

print(df.sort_values(by="score",ascending=False))  #Các điểm sắp xếp giảm dần
print()

print(df.sort_values(by="score",ascending=True))  #Các điểm sắp xếp tăng dần
print()

def rank(score):
    if score >= 9:
        return "Xuat sac"
    elif score >= 8:
        return "Gioi"
    elif score >= 7:
        return "Kha"
    else:
        return "Trung binh"
df["rank"] = df["score"].apply(rank)  #Điểm kết quả
print(df)