#include <stdbool.h>

bool is_palindrome (char * string){
    int i = 0, k = 0, i1 = 0, k1 = 0;
    while (string[i] != '\0'){
        if (string[i] != ' ')
            k++;
        i++;
    }
    k1 = i;
    int string_1 [k];
    i = 0;
    while ( i < k1 ){
        if (string [i] != ' '){
            string_1[i1++] = string[i];
        }
        i++;
    }
    printf("%d\n", k/2);
    for (i = 0; i < k/2; i++){
        if (string_1[i] != string_1[k-i-1])
            return false;
    }
    return true;
}
