#include <iostream>
#define ll unsigned long long
ll f(ll n){
    if (n < 20)
        return n;
    return (n-6)*f(n-7);
}
int main(void){
    std::cout << ((f(47872)-290*f(47865))/f(47858)) << std::endl;
    return 0;
    }
