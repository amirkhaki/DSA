#include <iostream>

int divide(int a, int b) {
    if (a < 0) return -divide(-a, b);
    if (b < 0) return -divide(a, -b);
    if (a < b) return 0;
    return 1 + divide(a - b, b);
}

int main(){
	int divided, divisor;
	std::cin >> divided >> divisor;
	std::cout << divide(divided, divisor);
	return 0;
}
