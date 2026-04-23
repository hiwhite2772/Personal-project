#include <iostream>

int main()
{
    double x = (int)3.975923;  // 3
    char y = 99;  // c

    std::cout << x << std::endl;
    std::cout << y << std::endl;

    std::cout << (char)115 << std::endl; // s

    int correct = 8;
    int questions = 10;
    double score = correct / (double)questions * 100;  // 80

    std::cout << score << "%" << '\n';
    return 0;
}