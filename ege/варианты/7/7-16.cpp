#include <iostream>
#define ll long long

ll f(ll n){
    if (n >= 3)
        return 2*n + 6 + f(n-2);
    return 3;
}

int main(void){
    std::cout << f(3027) - f(3023) << std::endl;
    return 0;
}
