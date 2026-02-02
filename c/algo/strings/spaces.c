#include <stdio.h>

int spaces (char * string){
    int max = 0, i = 0, k = 0;
    while (string[i] != '\0'){
        while (string[i] == ' ' && string[i] != '\0'){
            k++;
            i++;
        }
        if (k > max) max = k;
        k = 0;
        i++;
    }
    return max;
}

#if 1
#define MAX 1000
int main(void){
    int N, i, j; char string[MAX], ch;
    printf("Enter a number of characters: ");
    scanf("%d", &N);
#if 0
    for (i = 0; i < N; i++){
        j = rand()%128;
        while ( j  < 32) j = rand()%128;
        string[i] = j;
    }
#endif
    for (i = 0; i < N; i++)
        string[i] = getchar();

    string[N] = '\0';
    for (i = 0; i < N; i++)
        putchar(string[i]);
    putchar('\n');
    printf("%d\n", spaces(string));
    return 0;
}
#endif
