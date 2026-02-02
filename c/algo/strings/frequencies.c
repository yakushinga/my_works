#include <stdio.h>
#include <stdlib.h>
#include "palindrome.c"
#define MAX 1000

void frequencies (char * str, int N){
    int characters [128], i;
    for (i=0; i < 128; i++)
        characters[i] = 0;
    for (i=0; i < N; i++)
        characters[str[i]]++;
    printf("Character | Frequency\n");
    printf("---------------------\n");
    for (i = 32; i < 127; i++)
        if (characters [i] > 0)
            printf("%9c | %9d\n", i, characters[i]);
}
#if 0

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
    frequencies(string, N);
    printf("%d\n", is_palindrome(string));
    return 0;
}
#endif
