// ============================================================
//  HelloCSharp.cs — Ví dụ C# cơ bản (có so sánh với Python)
//  Chạy: dotnet script HelloCSharp.cs  HOẶC  tạo project mới
// ============================================================
using System;
using System.Collections.Generic;
using System.Linq;
 
// ── 1. NAMESPACE & CLASS ──────────────────────────────────
// Python không cần class bắt buộc, C# thì cần
namespace HelloCSharp
{
    class Program
    {
        // Điểm bắt đầu chạy chương trình (giống if __name__ == "__main__" trong Python)
        static void Main(string[] args)
        {
            Console.WriteLine("=== 1. IN RA MÀN HÌNH ===");
            // Python: print("Hello, World!")
            Console.WriteLine("Hello, World!");
            Console.WriteLine($"Xin chào từ C#!");  // $ = f-string của Python
 
 
            // ── 2. BIẾN & KIỂU DỮ LIỆU ──────────────────────────
            Console.WriteLine("\n=== 2. BIẾN & KIỂU DỮ LIỆU ===");
 
            // Python: name = "Minh"   (không cần khai báo kiểu)
            string name = "Minh";           // C# phải khai báo kiểu rõ ràng
            int age = 25;
            double gpa = 3.75;
            bool isStudent = true;
 
            // var = tự suy kiểu (giống Python hơn)
            var city = "Hồ Chí Minh";       // C# tự biết đây là string
 
            Console.WriteLine($"Tên: {name}, Tuổi: {age}, GPA: {gpa}, Sinh viên: {isStudent}");
            Console.WriteLine($"Thành phố: {city}");
 
 
            // ── 3. IF / ELSE ──────────────────────────────────────
            Console.WriteLine("\n=== 3. ĐIỀU KIỆN IF/ELSE ===");
 
            // Python: if age >= 18:
            if (age >= 18)                  // C# dùng () và {}
            {
                Console.WriteLine($"{name} đã đủ 18 tuổi");
            }
            else
            {
                Console.WriteLine($"{name} chưa đủ 18 tuổi");
            }
 
 
            // ── 4. VÒNG LẶP ──────────────────────────────────────
            Console.WriteLine("\n=== 4. VÒNG LẶP ===");
 
            // Python: for i in range(5):
            for (int i = 0; i < 5; i++)
            {
                Console.Write($"{i} ");
            }
            Console.WriteLine();
 
            // foreach — giống for item in list của Python
            string[] fruits = { "Xoài", "Ổi", "Mít", "Sầu riêng" };
            foreach (string fruit in fruits)
            {
                Console.Write($"{fruit} ");
            }
            Console.WriteLine();
 
            // while — giống Python
            int count = 0;
            while (count < 3)
            {
                Console.Write($"while:{count} ");
                count++;
            }
            Console.WriteLine();
 
 
            // ── 5. HÀM (METHODS) ─────────────────────────────────
            Console.WriteLine("\n=== 5. HÀM ===");
 
            // Python: def greet(name): return f"Chào {name}!"
            // C# khai báo kiểu trả về (string, int, void...)
            string greeting = Greet("Lan");
            Console.WriteLine(greeting);
 
            int sum = Add(10, 20);
            Console.WriteLine($"10 + 20 = {sum}");
 
 
            // ── 6. LIST & DICTIONARY ─────────────────────────────
            Console.WriteLine("\n=== 6. LIST & DICTIONARY ===");
 
            // Python: my_list = [1, 2, 3]
            List<int> numbers = new List<int> { 1, 2, 3, 4, 5 };
            numbers.Add(6);
            Console.WriteLine($"List: {string.Join(", ", numbers)}");
 
            // Python: my_dict = {"a": 1, "b": 2}
            Dictionary<string, int> scores = new Dictionary<string, int>
            {
                { "Toán", 9 },
                { "Văn", 8 },
                { "Anh", 10 }
            };
            foreach (var item in scores)
            {
                Console.WriteLine($"  {item.Key}: {item.Value} điểm");
            }
 
 
            // ── 7. LINQ (siêu mạnh, Python dùng list comprehension) ──
            Console.WriteLine("\n=== 7. LINQ ===");
 
            // Python: evens = [x for x in numbers if x % 2 == 0]
            var evens = numbers.Where(x => x % 2 == 0).ToList();
            Console.WriteLine($"Số chẵn: {string.Join(", ", evens)}");
 
            // Python: doubled = [x * 2 for x in evens]
            var doubled = evens.Select(x => x * 2).ToList();
            Console.WriteLine($"Nhân đôi: {string.Join(", ", doubled)}");
 
            int total = numbers.Sum();
            Console.WriteLine($"Tổng: {total}");
 
 
            // ── 8. CLASS & OBJECT ─────────────────────────────────
            Console.WriteLine("\n=== 8. CLASS & OBJECT ===");
 
            Student student = new Student("An", 20, "CNTT");
            student.Introduce();
            Console.WriteLine($"Email: {student.GetEmail()}");
 
 
            Console.WriteLine("\n✅ Xong! Bạn đã chạy qua 8 khái niệm cơ bản của C#");
        }
 
 
        // ── ĐỊNH NGHĨA HÀM (đặt trong class Program) ─────────────
        // Python: def greet(name): return f"Chào {name}!"
        static string Greet(string name)
        {
            return $"Chào {name}!";
        }
 
        // Python: def add(a, b): return a + b
        static int Add(int a, int b)
        {
            return a + b;
        }
    }
 
 
    // ── ĐỊNH NGHĨA CLASS RIÊNG ────────────────────────────────────
    // Python:
    // class Student:
    //     def __init__(self, name, age, major):
    //         self.name = name
    //         ...
    class Student
    {
        // Properties (thuộc tính) — Python dùng self.name
        public string Name { get; set; }
        public int Age { get; set; }
        public string Major { get; set; }
 
        // Constructor — giống __init__ trong Python
        public Student(string name, int age, string major)
        {
            Name = name;
            Age = age;
            Major = major;
        }
 
        // Method — giống def trong Python
        public void Introduce()
        {
            Console.WriteLine($"Mình là {Name}, {Age} tuổi, ngành {Major}");
        }
 
        public string GetEmail()
        {
            // Python: return f"{self.name.lower()}@student.edu.vn"
            return $"{Name.ToLower()}@student.edu.vn";
        }
    }
}

/*  
  File HelloCSharp.cs đã sẵn sàng! Mình viết theo hướng so sánh trực tiếp với Python để bạn dễ liên hệ. 
  File gồm 8 phần:

  In ra màn hình (print → Console.WriteLine)
  Biến & kiểu dữ liệu (C# khai báo kiểu, Python thì không)
  If/else
  Vòng lặp for, foreach, while
  Hàm (phải khai báo kiểu trả về)
  List & Dictionary
  LINQ — tương đương list comprehension của Python, rất mạnh
  Class & Object

  `Để chạy thử, bạn cần cài .NET SDK rồi chạy:
  bashdotnet new console -n HelloProject
  # copy nội dung file vào Program.cs
  dotnet run
  
*/
