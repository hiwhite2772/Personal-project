#include <iostream>

int main() {
    double PI = 3.14;
    double radius = 10;
    const double circumference = 2 * PI * radius;

    std::cout << circumference << " cm";
    return 0;
}