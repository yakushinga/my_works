#include <iostream>
#define ull unsigned long long
ull f(ull n){
    if (n >= 2025)
        return n;
    return 2*n + f(n + 2);
}
int main(void){
    std::cout << f(82)- f(81) << std::endl;
    return 0;
}
