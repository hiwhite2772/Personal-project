#include <iostream>
#include <cmath>

int main()
{
    double x = 9.67;
    double y = 16;
    double z;

    z = std::min(x, y);  // 9
    z = std::max(x, y);  // 16
    z = abs(-4);  // 4
    z = pow(4, 2);  // 16
    z = sqrt(16);  // 4
    z = round(x);  // 10
    z = ceil(x);  // 10
    z = floor(x);  // 9

    std::cout << z << '\n';
    return 0;
}