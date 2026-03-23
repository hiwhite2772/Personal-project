import random
secret = random.randint(1, 100)
count = 0
while count < 7:
    guess = int(input("Nhập số n (đúng 7 lần) = "))
    count += 1
    if guess < secret:
        print("Số nhỏ quá!")
    elif guess > secret:
        print("Số lớn quá")
    else:
        print(f"Wow! Bạn đoán chính xác rồi! Sau {count} lần!")
        break
if count == 7 and guess != secret:
    print(f"Tiếc quá! Bạn sẽ cố gắng đoán số chính xác! Con số bí mật: {secret}")

