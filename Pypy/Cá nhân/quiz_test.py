questions = ("Should you use smoking to relax?",
            "How many hours of sleep to suitable for young people?", 
            "What is the most important meal of the day?",
            "Where is the best place to exercise?", 
            "Who is the founder of Microsoft?"
            )
options = (("A. Noway", "B. Not", "C. Banned", "D. Yes"),
           ("A. 7p.m", "B. 10p.m", "C. 3a.m", "D. 12a.m"),
           ("A. vegetable", "B. fast food", "C. coca", "D. sugar"),
           ("A. at libraby", "B. at restaurant", "C. at park", "D. at cafe"),
           ("A. Bill Gates", "B. Beyoncé", "C. Auta", "D. Vaniessa"))
answers = ("C", "B", "A", "C", "A")
guesses = []
score = 0
question_num = 0

for q in questions:  #1 trong những câu hỏi
    print("-------------------")
    print(q)

    for o in options[question_num]:  #1 trong những câu lựa chọn đáp án cùng câu hỏi đó
        print(o)

    #Vòng lặp kiểm tra đáp án hợp lệ
    while True:
        guess = input("Nhập chọn 1 đáp án (A/B/C/D): ").upper().strip()

        if guess in ("A", "B", "C", "D"):  #Kiểm tra có A, B, C, D hay không?
            break
        else:
            print("Vui lòng chỉ nhập A, B, C hoặc D!")

    guesses.append(guess)  #Người ta chọn câu đáp án thì thêm vào danh sách đã chọn đáp án đó

    if guess == answers[question_num]:  #Nếu kiểm tra trả lời đáp án đã chọn của người ta thì đúng hay sai?
        score += 1
        print("Chính xác!")
    else:
        print("Sai rồi!")
        print(f"Đáp án chuẩn: {answers[question_num]}")

    question_num += 1

print("-------------------")
print("|Kết quả cuối cùng|")
print("-------------------")
print("Đáp án chuẩn:", end=" ")

for a in answers:
    print(a, end=" ")
print()
print("Đáp án đã chọn của bạn:", end=" ")

for g in guesses:
    print(g, end=" ")
print()

score = int(score / len(questions) * 100)  #Điểm = (số câu đáp án đúng / Số câu hỏi) nhân 100
print(f"Điểm số của bạn là: {score}%")

"""
**Phần thay đổi chính:**
Thay dòng `guess = input(...).upper()` bằng vòng `while True` với logic:
- Nhập và `.strip()` để loại khoảng trắng thừa
- Kiểm tra `if guess in ("A", "B", "C", "D")` → hợp lệ thì `break` thoát vòng lặp
- Ngược lại in cảnh báo và yêu cầu nhập lại

Ví dụ khi chạy:
Nhập chọn 1 đáp án (A/B/C/D): x
⚠️  Vui lòng chỉ nhập A, B, C hoặc D!
Nhập chọn 1 đáp án (A/B/C/D): 5
⚠️  Vui lòng chỉ nhập A, B, C hoặc D!
Nhập chọn 1 đáp án (A/B/C/D): A
Chính xác!
"""