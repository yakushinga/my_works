#include <stdio.h>
#include <string.h>
#include "stack_array.h"
#include "inf_to_postf.c"

int calculate_postfix (char * a){
    int i, N = strlen(a);
    STACKinit(N);
    for (i = 0; i < N; i++){
        if (a[i] == '+')
            STACKpush(STACKpop()+STACKpop());
        if (a[i] == '*')
            STACKpush(STACKpop()*STACKpop());
        if ((a[i] >= '0') && (a[i] <='9'))
            STACKpush(a[i]-'0');
        }
    return STACKpop();
}

#if 0
int main(void){
    char a[100];
    char * p;
    printf("Enter the expression in the infix form: ");
    scanf("%s", a);
    a[99]='\0';
    p = inf_to_postf(a);
    printf("%s\n", p);
    printf("%d\n", calculate_postfix(p));
    return 0;
}
#endif
