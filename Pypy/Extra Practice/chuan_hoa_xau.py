def normalize(s):
    # Chuẩn hoá khoảng trắng
    s = s.strip()  # Bỏ khoảng trắng thừa ở đầu và cuối câu
    s = " ".join(s.split())  #

    # Chuẩn hoá dấu câu
    res = ""
    i = 0
    while i < len(s):
        if s[i] in "!.?:,":
            if res and res[-1] == " ":
                res = res[:-1]
                
            res += s[i]
            i += 1

            while i < len(s) and s[i] == " ":  # Bỏ dấu cách phía sau dấu câu
                i += 1
                
            if i < len(s):  # Thêm đúng 1 dấu cách sau dấu câu nếu chưa hết chuỗi
                res += " "
            continue    
            
        else:
            res += s[i]
        i += 1

    # Chuẩn hoá chữ in hoa đầu câu
    result = ""
    capitalize_next = True

    for c in res:  # Duyệt từng ký tự
        if c.isalpha():  # Nếu là chữ cái
            if capitalize_next:
                result += c.upper()  # Nếu cần chữ in hoa
                capitalize_next = False
            else:
                result += c.lower()  # Còn lại đều chữ thường
        else:  # Nếu không phải chữ cái
            result += c
            if c in "!.?:":  # Sau gặp dấu câu có viết chữ hoa
                capitalize_next = True

    return result.strip()

with open("Bai1.inp", "r") as f:
    raw = f.readline().rstrip("\n")
    
normalized = normalize(raw)

with open("Bai1.out", "w") as f:
    # So sánh chuỗi nhập so với chuỗi xử lý điều kiện
    if raw == normalized:
        f.write("1\n*")
    else:
        f.write("0\n" + normalized)