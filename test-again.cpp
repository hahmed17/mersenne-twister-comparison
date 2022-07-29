#include <iostream>
#include <random>

int main()
{
    std::mt19937 e2(12345);
    std::cout << e2() << std::endl;
}