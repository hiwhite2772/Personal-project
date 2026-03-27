// ============================================================
//  HelloC.c — Ví dụ ngôn ngữ C cơ bản (có so sánh với Python)
//  Biên dịch: gcc HelloC.c -o HelloC
//  Chạy:      ./HelloC   (Linux/Mac)  hoặc  HelloC.exe (Windows)
// ============================================================

/*
    Ngôn ngữ C ra đời năm 1972 — là "cha đẻ" của C#, Java, Python...
    C chạy rất nhanh, gần với phần cứng, không có garbage collector.
    Bạn phải tự quản lý bộ nhớ — đây là điểm khác lớn nhất với Python.
*/

#include <stdio.h>      /* printf, scanf — thư viện xuất nhập chuẩn */
#include <stdlib.h>     /* malloc, free  — cấp phát bộ nhớ động     */
#include <string.h>     /* strcpy, strlen — xử lý chuỗi             */
#include <stdbool.h>    /* bool, true, false                         */

/* ── KHAI BÁO HÀM TRƯỚC KHI DÙNG (C yêu cầu điều này) ── */
int add(int a, int b);
void greet(char name[]);
void demo_array();
void demo_pointer();
void demo_struct();


/* ── ĐIỂM BẮT ĐẦU CHƯƠNG TRÌNH ── */
/* Python: if __name__ == "__main__":  */
int main() {

    /* ── 1. IN RA MÀN HÌNH ── */
    printf("=== 1. IN RA MAN HINH ===\n");
    /* Python: print("Hello, World!")  */
    printf("Hello, World!\n");       /* \n = xuống dòng */
    printf("Xin chao tu ngon ngu C!\n");


    /* ── 2. BIẾN & KIỂU DỮ LIỆU ── */
    printf("\n=== 2. BIEN & KIEU DU LIEU ===\n");

    /*
        Python: name = "Minh"  (tự động nhận kiểu)
        C:      phải khai báo kiểu TRƯỚC, và KHÔNG thay đổi được kiểu sau đó
    */
    int age       = 25;
    float gpa     = 3.75f;
    double pi     = 3.14159265;
    char grade    = 'A';            /* char chỉ chứa 1 ký tự, dùng nháy đơn */
    bool isPass   = true;

    /* Chuỗi trong C = mảng ký tự (KHÁC với Python rất nhiều) */
    char name[50] = "Minh";        /* cấp 50 ô nhớ cho chuỗi tối đa 49 ký tự */

    /* Python: print(f"Tên: {name}, Tuổi: {age}") */
    printf("Ten: %s, Tuoi: %d, GPA: %.2f\n", name, age, gpa);
    printf("Diem: %c, Dau: %s\n", grade, isPass ? "Co" : "Khong");

    /*
        FORMAT SPECIFIER — thứ C# và Python không cần nhớ:
        %d  = int          %f  = float/double
        %s  = string       %c  = char
        %ld = long         %lf = double (trong scanf)
        %.2f = 2 chữ số thập phân
    */


    /* ── 3. NHẬP TỪ BÀN PHÍM ── */
    /*
        Python: x = int(input("Nhập số: "))
        C:      printf rồi scanf riêng, phải dùng & (địa chỉ biến)
    */
    int x;
    printf("\n=== 3. NHAP TU BAN PHIM ===\n");
    printf("Nhap mot so nguyen: ");
    scanf("%d", &x);               /* & = lấy địa chỉ của biến x */
    printf("Ban vua nhap: %d\n", x);


    /* ── 4. IF / ELSE ── */
    printf("\n=== 4. DIEU KIEN IF/ELSE ===\n");

    /* Python: if age >= 18: */
    if (age >= 18) {
        printf("%s da du 18 tuoi\n", name);
    } else {
        printf("%s chua du 18 tuoi\n", name);
    }

    /* switch/case — C# cũng có, Python thì dùng match (3.10+) */
    switch (grade) {
        case 'A': printf("Xuat sac!\n"); break;
        case 'B': printf("Kha!\n");      break;
        case 'C': printf("Trung binh\n");break;
        default:  printf("Yeu\n");
    }


    /* ── 5. VÒNG LẶP ── */
    printf("\n=== 5. VONG LAP ===\n");

    /* Python: for i in range(5): */
    for (int i = 0; i < 5; i++) {
        printf("%d ", i);
    }
    printf("\n");

    /* while — giống Python */
    int count = 0;
    while (count < 3) {
        printf("while:%d ", count);
        count++;
    }
    printf("\n");

    /* do...while — chạy ít nhất 1 lần (Python không có) */
    int n = 0;
    do {
        printf("do-while:%d ", n);
        n++;
    } while (n < 3);
    printf("\n");


    /* ── 6. HÀM ── */
    printf("\n=== 6. HAM ===\n");

    int result = add(10, 20);
    printf("10 + 20 = %d\n", result);
    greet("Lan");


    /* ── 7. MẢNG (ARRAY) ── */
    demo_array();


    /* ── 8. CON TRỎ (POINTER) — đặc trưng của C ── */
    demo_pointer();


    /* ── 9. STRUCT — tương tự class đơn giản của Python ── */
    demo_struct();


    printf("\n✓ Xong! Ban da chay qua 9 khai niem co ban cua C\n");
    return 0;   /* trả về 0 = chạy thành công */
}


/* ============================================================
   ĐỊNH NGHĨA CÁC HÀM
   ============================================================ */

/* Python: def add(a, b): return a + b */
int add(int a, int b) {
    return a + b;
}

/* Python: def greet(name): print(f"Chào {name}!") */
void greet(char name[]) {   /* void = không trả về gì */
    printf("Chao %s!\n", name);
}


/* ── 7. MẢNG ── */
void demo_array() {
    printf("\n=== 7. MANG (ARRAY) ===\n");

    /*
        Python: nums = [10, 20, 30, 40, 50]
        C: phải khai báo kích thước cố định TRƯỚC
    */
    int nums[5] = {10, 20, 30, 40, 50};
    int size = 5;

    /* Duyệt mảng */
    for (int i = 0; i < size; i++) {
        printf("nums[%d] = %d\n", i, nums[i]);
    }

    /* Tính tổng */
    int total = 0;
    for (int i = 0; i < size; i++) {
        total += nums[i];
    }
    printf("Tong: %d\n", total);

    /*
        QUAN TRỌNG: C không kiểm tra giới hạn mảng!
        nums[10] sẽ không báo lỗi mà đọc vùng nhớ sai → nguy hiểm
        Python sẽ báo IndexError ngay lập tức
    */
}


/* ── 8. CON TRỎ — thứ làm C khác hoàn toàn Python ── */
void demo_pointer() {
    printf("\n=== 8. CON TRO (POINTER) ===\n");

    /*
        Python không có con trỏ tường minh.
        Con trỏ trong C = biến lưu ĐỊA CHỈ ô nhớ của biến khác.
        Dùng để: truyền biến vào hàm theo tham chiếu, cấp phát bộ nhớ động
    */
    int a = 42;
    int *p = &a;    /* p trỏ đến địa chỉ của a */
                    /* & = lấy địa chỉ, * = lấy giá trị tại địa chỉ */

    printf("Gia tri a    = %d\n", a);
    printf("Dia chi cua a = %p\n", (void*)p);
    printf("Gia tri qua p = %d\n", *p);   /* *p đọc giá trị tại địa chỉ p */

    *p = 99;   /* thay đổi a thông qua con trỏ */
    printf("a sau khi doi qua con tro = %d\n", a);

    /* ── Cấp phát bộ nhớ động ── */
    /*
        Python: my_list = []  (tự động mở rộng)
        C: phải tự xin bộ nhớ (malloc) và trả lại (free)
    */
    int *arr = (int*)malloc(3 * sizeof(int));  /* xin 3 ô int */
    if (arr == NULL) {
        printf("Het bo nho!\n");
        return;
    }
    arr[0] = 100;
    arr[1] = 200;
    arr[2] = 300;
    printf("Mang dong: %d %d %d\n", arr[0], arr[1], arr[2]);
    free(arr);   /* PHẢI free sau khi dùng xong, không thì rò bộ nhớ (memory leak) */
}


/* ── 9. STRUCT ── */
void demo_struct() {
    printf("\n=== 9. STRUCT ===\n");

    /*
        Python:
        class Student:
            def __init__(self, name, age, gpa):
                self.name = name
                ...

        C không có class, dùng struct để nhóm dữ liệu lại
        (không có method, không có kế thừa như C# hay Python)
    */
    typedef struct {
        char name[50];
        int  age;
        float gpa;
    } Student;

    Student s1;
    strcpy(s1.name, "An");   /* chuỗi không gán = được, phải dùng strcpy */
    s1.age = 20;
    s1.gpa = 3.8f;

    printf("Ten: %s\n", s1.name);
    printf("Tuoi: %d\n",  s1.age);
    printf("GPA: %.1f\n", s1.gpa);

    /*
        Mảng struct — giống list of objects trong Python
        Python: students = [Student("An",20,3.8), Student("Bình",21,3.5)]
    */
    Student students[2] = {
        {"An",   20, 3.8f},
        {"Binh", 21, 3.5f}
    };
    for (int i = 0; i < 2; i++) {
        printf("SV%d: %s - %.1f GPA\n", i+1, students[i].name, students[i].gpa);
    }
}

/*
`File HelloC.c xong rồi! Cũng có so sánh Python xuyên suốt.
Gồm 9 phần:

In ra màn hình — printf thay vì print, phải dùng %d, %s, %f...
Biến & kiểu dữ liệu — khai báo kiểu bắt buộc, chuỗi là mảng ký tự
Nhập từ bàn phím — scanf + dấu & (khác Python hoàn toàn)
If/else + switch/case
Vòng lặp — thêm do...while mà Python không có
Hàm — phải khai báo trước khi dùng
Mảng — kích thước cố định, không tự mở rộng như list Python
Con trỏ ⚠️ — phần khó nhất và đặc trưng nhất của C, Python không có
Struct — thay thế cho class, nhưng không có method

`Để chạy thử, cần cài GCC:
bashgcc HelloC.c -o HelloC
./HelloC

*/