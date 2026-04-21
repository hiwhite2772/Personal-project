#Tìm độ dài dãy con liên tiếp tăng dần dài nhất trong chuỗi

t = int(input())  #Số lượng test case

for _ in range(t):

    s = input().strip()
    
    current_len = 1  #Độ dài đoạn tăng hiện tại (ít nhất là 1 ký tự)
    max_len = 1  #Độ dài lớn nhất tìm được
    
    #Duyệt từ ký tự thứ 2
    for i in range(1, len(s)):
        
        #Nếu ký tự hiện tại lớn hơn ký tự trước -> tiếp tục chuỗi tăng
        if s[i] > s[i-1]:
            current_len += 1
        #Nếu nhỏ hơn hoặc bằng thì chuỗi bị gãy -> reset lại ban đầu
        else:
            current_len = 1
        
        #Cập nhật kết quả lớn nhất
        max_len = max(max_len, current_len)

    print(max_len)


"""
## Ví dụ chạy thử:
`Input:
1
abcaefg

`Quá trình:
a → b → c (tăng → length = 3)
c → a (reset)
a → e → f → g (tăng → length = 4)
`Output:
4

## Độ phức tạp:
Thời gian: O(n) cho mỗi chuỗi
Bộ nhớ: O(1)
`Rất tối ưu (chỉ duyệt 1 lần)

## Tóm lại:
`Đây là bài:
- Dạng: String + Greedy / Linear Scan
- Mục tiêu: Tìm đoạn con liên tiếp tăng dần dài nhất
- Kỹ thuật chính:
+ So sánh từng cặp ký tự liên tiếp
+ Dùng biến để track độ dài hiện tại và max


"""