# Tổng hợp các bài toán đã học

## Mục lục
1. [Two Sum – Hai số có tổng bằng target](#1-two-sum--hai-số-có-tổng-bằng-target)
2. [Palindrome Number – Số nguyên đối xứng](#2-palindrome-number--số-nguyên-đối-xứng)
3. [Arithmetic Progression – Mảng có thể thành cấp số cộng](#3-arithmetic-progression--mảng-có-thể-thành-cấp-số-cộng)
4. [Pivot Integer – Số nguyên chốt](#4-pivot-integer--số-nguyên-chốt)
5. [Ugly Number – Số xấu](#5-ugly-number--số-xấu)
6. [Smallest Repunit Divisible by K – Số chỉ chứa 1 chia hết cho K](#6-smallest-repunit-divisible-by-k--số-chỉ-chứa-1-chia-hết-cho-k)
7. [Self Dividing Numbers – Số tự chia hết](#7-self-dividing-numbers--số-tự-chia-hết)

---

## 1. Two Sum – Hai số có tổng bằng target

**Mô tả:**  
Cho một mảng các số nguyên `nums` và một số nguyên `target`, hãy tìm **hai chỉ số** sao cho tổng hai phần tử tại hai chỉ số đó bằng `target`.  
- Mỗi input **chỉ có duy nhất một đáp án**.  
- Không được sử dụng cùng một phần tử hai lần.  
- Trả về danh sách chỉ số `[i, j]` theo bất kỳ thứ tự nào.

**Ví dụ:**
```text
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Input: nums = [3,2,4], target = 6
Output: [1,2]

Input: nums = [3,3], target = 6
Output: [0,1]
```

---

## 2. Palindrome Number – Số nguyên đối xứng

**Mô tả:**
Cho một số nguyên x, trả về True nếu x là số đối xứng (đọc xuôi ngược giống nhau), ngược lại trả về False.

**Ví dụ:**
```text
Input: x = 121
Output: True

Input: x = -121
Output: False

Input: x = 10
Output: False
```

---

## 3. Arithmetic Progression – Mảng có thể thành cấp số cộng

**Mô tả:**
Một dãy số được gọi là cấp số cộng nếu hiệu giữa hai phần tử liên tiếp luôn giống nhau.
Cho một mảng arr, trả về True nếu có thể sắp xếp lại mảng để tạo thành cấp số cộng, ngược lại trả về False.

**Ví dụ:**
```text
Input: arr = [3,5,1]
Output: True
# vì sort([3,5,1]) = [1,3,5], hiệu = 2

Input: arr = [1,2,4]
Output: False
```

---

## 4. Pivot Integer – Số nguyên chốt

**Mô tả:**
Cho một số nguyên dương n, tìm số nguyên x sao cho:

Tổng các số từ 1 đến x = Tổng các số từ x đến n
Nếu tồn tại, trả về x.
Nếu không tồn tại, trả về -1.
Đảm bảo rằng tối đa một số chốt tồn tại với dữ liệu input.

**Ví dụ:**
```text
Input: n = 8
Output: 6
# 1+2+3+4+5+6 = 6+7+8 = 21

Input: n = 4
Output: -1
```

---

## 5. Ugly Number – Số xấu

**Mô tả:**
Một số nguyên dương n được gọi là số xấu (ugly number) nếu chỉ có thừa số nguyên tố 2, 3, hoặc 5.

Trả về True nếu n là số xấu, ngược lại False.

**Ví dụ:**
```text
Input: n = 6
Output: True
# 6 = 2*3

Input: n = 14
Output: False
# 14 = 2*7 (7 không phải 2,3,5)

Input: n = 1
Output: True
# 1 mặc định là ugly number
```

---

## 6. Smallest Repunit Divisible by K – Số chỉ chứa 1 chia hết cho K

**Mô tả:**
Cho số nguyên dương k, tìm số nguyên nhỏ nhất n chỉ chứa chữ số 1 sao cho n % k == 0.

Trả về độ dài của n.
Nếu không tồn tại, trả về -1.
Lưu ý: n có thể quá lớn để lưu trong kiểu integer thông thường.

**Ví dụ:**
```text
Input: k = 3
Output: 3
# n = 111 chia hết cho 3

Input: k = 2
Output: -1
# không thể chia hết vì n chỉ có chữ số 1
```

---

## 7. Self Dividing Numbers – Số tự chia hết

**Mô tả:**
Một số nguyên dương n được gọi là tự chia hết nếu:

Không chứa chữ số 0
Chia hết cho tất cả các chữ số của nó

Cho hai số nguyên left và right, trả về danh sách tất cả số tự chia hết trong [left, right].

**Ví dụ:**
```text
Input: left = 1, right = 22
Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]

Input: left = 47, right = 85
Output: [48,55,66,77]
```