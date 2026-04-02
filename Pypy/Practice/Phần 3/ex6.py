def xep_loai(diem):
    if diem >= 9:
        return "Gioi"
    elif diem >= 7:
        return "Kha"
    elif diem >= 5:
        return "Trung binh"
    
def doc_file(ten_file):
    ds = []
    with open(ten_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            parts = line.split(",")
            ten = parts[0].strip()
            diem = float(parts[1].strip())
            ds.append((ten, diem))
    return ds

def ghi_file(ds, ten_file):
    with open(ten_file, "w", encoding="utf-8") as f:
        for ten, diem in ds:
            if diem >= 5:
                loai = xep_loai(diem)
                f.write(f"{ten} - {int(diem)} - {loai}\n")
        print("Da ghi xong file dat.txt")

ds = doc_file("diem.txt")
ghi_file(ds, "dat.txt")