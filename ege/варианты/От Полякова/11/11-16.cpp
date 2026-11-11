#include <iostream>
#define ull unsigned long long

ull f(ull n){
    if (n < 5)
        return n;
    return 2*n*f(n-4);
}

int main(void){
    std::cout << (f(13766)-9*f(13762))/f(13758) << std::endl;
    return 0;
}
