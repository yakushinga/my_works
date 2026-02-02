#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "min_to_start.c"
#include "max_to_end.c"
#include "swap_nodes.c"
#include "copy_list.c"
#include "selection.c"

bool parity (link t);
bool prime (link t);
void print(link t);

int main (int argc, char * argv[]){
    int N = atoi(argv[1]);
    link t, x, max, new;
    int i, integer;

    for (i = 0; i < N; i++){
        if (i==0){
            t = malloc(sizeof *t);
            x=t;
        }
        else{
            t->next = malloc(sizeof *t);
            t=t->next;
        }
        printf("Insert an integer: ");
        scanf("%d", &integer);
        t->item = integer;
    }
    t->next=t;
    print(x);
    t = x;
    t = selection(t, prime);
    print(t);
    return 0;
}

bool parity (link t){
    return (t->item % 2 == 0);
}

bool prime (link t){
    if (t->item < 2)
        return false;
    Item i, el = t->item;
    for (i = 2; i*i<=el; i++){
        if (el % i == 0)
            return false;
    }
    return true;
}

void print(link t){
    while (t->next != t){
        printf ("%d ", t->item);
        t = t->next;
    }
    printf("%d\n", t->item);
}
