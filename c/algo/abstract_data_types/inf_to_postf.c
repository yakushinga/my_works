#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "stack.h"
#include "stack_array.h"

char * inf_to_postf(char * a){
    int N = strlen(a), i, j;
    char * postf = malloc((N+1)*sizeof(char));
    STACKinit(N);
    for(i = 0, j = 0; i < N; i++){
        if (a[i] == ')')
            postf[j++] = STACKpop();
        if ((a[i] == '+') || (a[i] == '*'))
            STACKpush(a[i]);
        if ((a[i] >= '0') && (a[i] <= '9'))
            postf[j++] = a[i];
    }
    if(!STACKempty())
        postf[j++] = STACKpop();
    postf[j] = '\0';
    return postf;
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

    return 0;
}
#endif
