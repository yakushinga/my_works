#include <iostream>
#define ull unsigned long long
ull f(int n, bool f13, bool f15){
    if (n == 51 && f13 && f15)
        return 1;
    if (n >= 51)
        return 0;
    if (n == 35)
        return 0;
    if (n == 13)
        f13 = true;
    if (n == 15)
        f15 = true;
    return f(n + 1, f13, f15) + f(n + 2, f13, f15) + f(n * 2, f13, f15);
}

int main(void){
    using namespace std;
    cout << f(7, false, false) << endl;
    return 0;
}
