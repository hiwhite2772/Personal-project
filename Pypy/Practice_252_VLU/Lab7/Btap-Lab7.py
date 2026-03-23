import pandas as pd
#1 - Đọc file dữ liệu
df = pd.read_csv("data.csv")
print(df)
print()
#2 - In ra 5 dòng đầu tiên của dữ liệu
print(df.head())
print()
#3 - Điểm trung bình theo 4 môn
df["diem_tb"] = (
    df["diem_toan"] + 
    df["diem_ly"] + 
    df["diem_hoa"] + 
    df["diem_sinh"]
) / 4
print(round(df, 2))
print()
#4 - Xếp loại theo điểm trung bình
def xep_loai(diem_tb):
    if diem_tb >= 8.0:
        return "Giỏi"
    elif 6.5 <= diem_tb < 8.0:
        return "Khá"
    else:
        return "Trung bình"
df["xep_loai"] = df["diem_tb"].apply(xep_loai)
print(round(df, 2))
print()
#5 - Lọc ra danh sách sinh viên Giỏi
print(round(df[df["xep_loai"] == "Giỏi"], 2))
print()
#6 - Điểm trung bình của từng ngành
print(round(df.groupby(df["nganh"])["diem_tb"].mean(), 2))
print()
#7 - Lưu dữ liệu đã xử lý
print(df.to_csv("diem_thi_xuly.csv", index=False))
