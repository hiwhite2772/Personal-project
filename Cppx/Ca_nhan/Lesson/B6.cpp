#include <iostream>

int main()
{
    double students = 20;
    int teachers = 20;
    int employee = 20;

    students = students + 1;  // 21
    teachers += 1;  // 21 
    employee++;  //21

    students = students - 1;  // 19
    teachers -= 1;  // 19
    employee--;  // 19

    students = students * 4;  // 80
    teachers *= 4;  // 80

    students = students / 3;  // 6.66667
    teachers /= 3;  // 6

    int a = 8 + 5 * 4 / 2;
    
    std::cout << students << '\n';
    std::cout << teachers << '\n';
    std::cout << employee << '\n';
    std::cout << a << '\n';
    return 0;
}