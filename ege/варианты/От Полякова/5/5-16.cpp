#include <iostream>
#define ull unsigned long long

ull g(ull n){
	if (n>=301208)
		return 10*n + 50;
	return g(n+7) - 21;
}

ull f(ull n){
	if (n > 40)
		return f(n-4) + 3020;
	return 3*(g(n-2)-15);
}

int main(void){
	std::cout << f(2026) << std::endl;
	return 0;
	}
