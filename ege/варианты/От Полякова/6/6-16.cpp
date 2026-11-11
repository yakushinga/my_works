#include <iostream>
#define ll long long

ll g(ll n){
    if (n >= 248045)
        return n/20 +28;
    return g(n + 9) - 4;
}

ll f(ll n){
    if (n>=19)
        return f(n-4) + 3580;
    return 6*(g(n-7)-36);
}

int main(void){
    std::cout << f(673) << std::endl;
    return 0;
}

