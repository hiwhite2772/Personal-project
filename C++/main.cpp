// ============================================================
//  HelloCPP.cpp — Ví dụ C++ cơ bản (so sánh với Python & C)
//  Biên dịch: g++ HelloCPP.cpp -o HelloCPP -std=c++17
//  Chạy:      ./HelloCPP   (Linux/Mac)  hoặc  HelloCPP.exe (Windows)
// ============================================================

/*
    C++ ra đời năm 1983 — là C được "nâng cấp" thêm OOP (lập trình hướng đối tượng).
    C++ = C  +  Class  +  Template  +  STL  +  nhiều thứ hiện đại hơn
    Dùng nhiều trong: game engine (Unreal), hệ thống nhúng, trình duyệt, AI/ML engine
*/

#include <iostream>     // cout, cin — thay thế printf/scanf của C
#include <string>       // string thực sự (không phải mảng char như C)
#include <vector>       // vector — giống list của Python
#include <map>          // map    — giống dict của Python
#include <algorithm>    // sort, find, max...
#include <memory>       // smart pointer (unique_ptr, shared_ptr)

using namespace std;    // để dùng cout thay vì std::cout cho ngắn gọn


// ── KHAI BÁO TRƯỚC (forward declaration) ──────────────────
int add(int a, int b);
void greet(string name);
void demo_vector();
void demo_map();
void demo_oop();
void demo_template();
void demo_smart_pointer();


// ── ĐIỂM BẮT ĐẦU CHƯƠNG TRÌNH ────────────────────────────
int main() {

    // ── 1. IN RA MÀN HÌNH ──────────────────────────────────
    cout << "=== 1. IN RA MAN HINH ===" << endl;

    // Python:  print("Hello!")
    // C:       printf("Hello!\n")
    // C++:     cout << "Hello!" << endl;
    cout << "Hello, World!" << endl;
    cout << "Xin chao tu C++!" << endl;

    // cout có thể nối nhiều thứ bằng <<
    string name = "Minh";
    int age = 25;
    cout << "Ten: " << name << ", Tuoi: " << age << endl;


    // ── 2. BIẾN & KIỂU DỮ LIỆU ────────────────────────────
    cout << "\n=== 2. BIEN & KIEU DU LIEU ===" << endl;

    // C++ có string thật sự — KHÁC C (C dùng mảng char)
    // Python: name = "Minh"
    string city     = "Ho Chi Minh";   // string đầy đủ tính năng
    int    score    = 95;
    double gpa      = 3.85;
    bool   isPass   = true;
    auto   pi       = 3.14159;         // auto = tự suy kiểu, giống var C#

    cout << "City: "  << city   << endl;
    cout << "Score: " << score  << endl;
    cout << "GPA: "   << gpa    << endl;
    cout << "Pass: "  << (isPass ? "Co" : "Khong") << endl;

    // C++17: structured binding — giống tuple unpacking Python
    // Python: a, b = 10, 20
    auto [a, b] = make_pair(10, 20);
    cout << "a=" << a << ", b=" << b << endl;


    // ── 3. NHẬP TỪ BÀN PHÍM ───────────────────────────────
    cout << "\n=== 3. NHAP TU BAN PHIM ===" << endl;

    // Python: x = int(input("Nhap so: "))
    // C:      scanf("%d", &x)
    // C++:    cin >> x
    int x;
    cout << "Nhap mot so nguyen: ";
    cin >> x;
    cout << "Ban vua nhap: " << x << endl;

    // Nhập chuỗi có khoảng trắng
    cin.ignore();                       // bỏ ký tự \n còn sót
    string fullname;
    cout << "Nhap ho ten: ";
    getline(cin, fullname);             // đọc cả dòng kể cả space
    cout << "Ho ten: " << fullname << endl;


    // ── 4. IF / ELSE & SWITCH ──────────────────────────────
    cout << "\n=== 4. DIEU KIEN ===" << endl;

    if (age >= 18) {
        cout << name << " da du 18 tuoi" << endl;
    } else if (age >= 13) {
        cout << name << " la thanh thieu nien" << endl;
    } else {
        cout << name << " con nho" << endl;
    }

    // C++17: if với khởi tạo biến bên trong
    if (int len = city.length(); len > 5) {
        cout << "Ten thanh pho dai: " << len << " ky tu" << endl;
    }


    // ── 5. VÒNG LẶP ───────────────────────────────────────
    cout << "\n=== 5. VONG LAP ===" << endl;

    // for thông thường
    for (int i = 0; i < 5; i++) {
        cout << i << " ";
    }
    cout << endl;

    // range-based for — giống for x in list của Python
    // Python: for fruit in fruits:
    vector<string> fruits = {"Xoai", "Oi", "Mit", "Sau rieng"};
    for (const string& fruit : fruits) {   // & = tham chiếu, tránh copy
        cout << fruit << " ";
    }
    cout << endl;

    // while
    int count = 0;
    while (count < 3) {
        cout << "while:" << count << " ";
        count++;
    }
    cout << endl;


    // ── 6. HÀM ────────────────────────────────────────────
    cout << "\n=== 6. HAM ===" << endl;

    cout << "10 + 20 = " << add(10, 20) << endl;
    greet("Lan");

    // Lambda — hàm ẩn danh, giống lambda Python nhưng mạnh hơn
    // Python: double = lambda x: x * 2
    auto doubleIt = [](int n) { return n * 2; };
    cout << "Double 7 = " << doubleIt(7) << endl;

    // Lambda capture — bắt biến từ ngoài vào
    int multiplier = 3;
    auto multiplyBy = [multiplier](int n) { return n * multiplier; };
    cout << "Triple 5 = " << multiplyBy(5) << endl;


    // ── 7. VECTOR & MAP ───────────────────────────────────
    demo_vector();
    demo_map();


    // ── 8. OOP — lập trình hướng đối tượng ───────────────
    demo_oop();


    // ── 9. TEMPLATE ───────────────────────────────────────
    demo_template();


    // ── 10. SMART POINTER ─────────────────────────────────
    demo_smart_pointer();


    cout << "\n✓ Xong! Ban da chay qua 10 khai niem co ban cua C++" << endl;
    return 0;
}


// ============================================================
//  ĐỊNH NGHĨA CÁC HÀM
// ============================================================

int add(int a, int b) {
    return a + b;
}

void greet(string name) {
    cout << "Chao " << name << "!" << endl;
}


// ── 7A. VECTOR ────────────────────────────────────────────
void demo_vector() {
    cout << "\n=== 7A. VECTOR (giong list Python) ===" << endl;

    // Python: nums = [1, 2, 3, 4, 5]
    vector<int> nums = {1, 2, 3, 4, 5};

    // Thêm / xoá phần tử
    nums.push_back(6);              // Python: nums.append(6)
    nums.pop_back();                // Python: nums.pop()
    nums.insert(nums.begin(), 0);   // Python: nums.insert(0, 0)

    // Duyệt
    cout << "Vector: ";
    for (int n : nums) cout << n << " ";
    cout << endl;

    // Kích thước
    cout << "Size: " << nums.size() << endl;     // Python: len(nums)

    // Sắp xếp
    // Python: nums.sort()
    sort(nums.begin(), nums.end());
    cout << "Sau sort: ";
    for (int n : nums) cout << n << " ";
    cout << endl;

    // Tìm kiếm
    // Python: if 3 in nums:
    auto it = find(nums.begin(), nums.end(), 3);
    if (it != nums.end()) {
        cout << "Tim thay gia tri 3" << endl;
    }

    // vector 2 chiều — giống list of list Python
    vector<vector<int>> matrix = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };
    cout << "Matrix[1][1] = " << matrix[1][1] << endl;  // = 5
}


// ── 7B. MAP ───────────────────────────────────────────────
void demo_map() {
    cout << "\n=== 7B. MAP (giong dict Python) ===" << endl;

    // Python: scores = {"Toan": 9, "Van": 8, "Anh": 10}
    map<string, int> scores = {
        {"Toan", 9},
        {"Van",  8},
        {"Anh",  10}
    };

    // Thêm / sửa
    scores["Ly"] = 7;               // Python: scores["Ly"] = 7

    // Duyệt
    for (const auto& [subject, score] : scores) {  // C++17 structured binding
        cout << subject << ": " << score << " diem" << endl;
    }

    // Kiểm tra key tồn tại
    // Python: if "Toan" in scores:
    if (scores.count("Toan")) {
        cout << "Co mon Toan, diem: " << scores["Toan"] << endl;
    }

    // Xoá
    scores.erase("Van");            // Python: del scores["Van"]
    cout << "Size sau xoa: " << scores.size() << endl;
}


// ── 8. OOP ────────────────────────────────────────────────
void demo_oop() {
    cout << "\n=== 8. OOP - HUONG DOI TUONG ===" << endl;

    /*
        C++ có OOP đầy đủ hơn C (vốn không có OOP)
        Gần giống Python nhưng phải khai báo kiểu rõ ràng hơn
    */

    // ── CLASS cơ bản ──────────────────────────────────────
    class Animal {
    public:
        string name;
        int    age;

        // Constructor — giống __init__ Python
        Animal(string n, int a) : name(n), age(a) {}

        // Method — giống def trong Python
        virtual void speak() {             // virtual = cho phép override
            cout << name << " keu..." << endl;
        }

        // Destructor — tự động gọi khi object bị xoá
        // Python có __del__ nhưng ít dùng
        virtual ~Animal() {}
    };

    // ── KẾ THỪA (Inheritance) ─────────────────────────────
    class Dog : public Animal {
    public:
        string breed;

        Dog(string n, int a, string b) : Animal(n, a), breed(b) {}

        // Override method — giống Python override
        void speak() override {
            cout << name << " keu: Go! Go!" << endl;
        }

        void fetch() {
            cout << name << " di nhat bong!" << endl;
        }
    };

    class Cat : public Animal {
    public:
        Cat(string n, int a) : Animal(n, a) {}

        void speak() override {
            cout << name << " keu: Meo! Meo!" << endl;
        }
    };

    // Tạo object
    Dog dog("Rex", 3, "Poodle");
    Cat cat("Mimi", 2);

    dog.speak();
    cat.speak();
    dog.fetch();

    cout << "Ten: " << dog.name << ", Giong: " << dog.breed << endl;

    // Polymorphism — đa hình
    // Python: animals = [Dog(...), Cat(...)]
    vector<Animal*> animals = {&dog, &cat};
    cout << "Da hinh: ";
    for (Animal* a : animals) {
        a->speak();                    // tự gọi đúng method của từng loại
    }
}


// ── 9. TEMPLATE ───────────────────────────────────────────
void demo_template() {
    cout << "\n=== 9. TEMPLATE ===" << endl;

    /*
        Template = hàm/class dùng được với nhiều kiểu dữ liệu
        Python không cần vì Python tự động nhận kiểu (dynamic typing)
        C++ cần vì phải khai báo kiểu rõ ràng
    */

    // Hàm template
    // Python: def get_max(a, b): return a if a > b else b
    auto getMax = []<typename T>(T a, T b) { return a > b ? a : b; };

    cout << "Max(3, 7)     = " << getMax(3, 7)         << endl;  // int
    cout << "Max(3.5, 2.1) = " << getMax(3.5, 2.1)     << endl;  // double
    cout << "Max(A, Z)     = " << getMax('A', 'Z')      << endl;  // char
}


// ── 10. SMART POINTER ─────────────────────────────────────
void demo_smart_pointer() {
    cout << "\n=== 10. SMART POINTER ===" << endl;

    /*
        C thuần: phải tự malloc/free → dễ quên → memory leak
        C++ hiện đại: dùng smart pointer, tự động giải phóng bộ nhớ
        Python:  tự động quản lý, không cần quan tâm

        unique_ptr = chỉ 1 chủ sở hữu, tự free khi ra khỏi scope
        shared_ptr = nhiều chủ sở hữu, free khi không ai dùng nữa
    */

    // unique_ptr
    // C cũ: int* p = malloc(sizeof(int));  ... free(p);
    unique_ptr<int> uptr = make_unique<int>(42);
    cout << "unique_ptr: " << *uptr << endl;
    // Không cần free — tự động giải phóng khi hàm kết thúc

    // shared_ptr
    shared_ptr<string> sptr1 = make_shared<string>("Hello C++");
    {
        shared_ptr<string> sptr2 = sptr1;   // cùng trỏ một vùng nhớ
        cout << "shared_ptr: " << *sptr1 << endl;
        cout << "So luong chu so huu: " << sptr1.use_count() << endl; // = 2
    } // sptr2 ra khỏi scope, use_count giảm còn 1
    cout << "Use count sau scope: " << sptr1.use_count() << endl;    // = 1
    // Khi sptr1 ra khỏi scope (cuối hàm), bộ nhớ tự giải phóng
}

/*
File HelloCPP.cpp xong!
Gồm 10 phần, có so sánh cả Python lẫn C:

In ra màn hình — cout << thay vì printf của C
Biến & kiểu dữ liệu — có auto, string thật sự (không phải mảng char như C)
Nhập từ bàn phím — cin >> thay vì scanf
If/else — thêm cú pháp C++17 hiện đại
Vòng lặp — có range-based for giống Python
Hàm + Lambda — lambda mạnh hơn Python, có thể "bắt" biến ngoài
Vector & Map — tương đương list và dict của Python
OOP — class, kế thừa, override, polymorphism
Template — hàm dùng được với mọi kiểu dữ liệu (Python không cần vì dynamic typing)
Smart Pointer — giải quyết vấn đề quản lý bộ nhớ thủ công của C

`Để chạy:
bashg++ HelloCPP.cpp -o HelloCPP -std=c++17
./HelloCPP
*/