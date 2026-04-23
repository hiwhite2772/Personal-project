#include <iostream>

int main(){
    std::string name;
    int age;

    std::cout << "How old are you?" << '\n';
    std::cin >> age;

    std::cout << "What's your name?" << '\n';
    std::getline(std::cin >> std::ws, name);  // getline() - đọc 1 dòng

    std::cout << "Hello " << name << '\n';
    std::cout << "You are " << age << " years old" << '\n';

    return 0;
}