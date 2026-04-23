#include <iostream>
#include <vector>

// typedef std::vector<std::pair<std::string, int>> pairlist_t;
typedef std::string text_t;
typedef int number_t;

using email = std::string;
using room = int;

int main() {
    text_t firstname = "HW";
    number_t score = 10;
    email Email = "HW20@gmail.com";
    room Room = 15;
    
    std::cout << firstname << '\n';
    std::cout << score << '\n';
    std::cout << Email << '\n';
    std::cout << Room << '\n';

    return 0;
}