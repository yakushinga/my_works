#include <stdlib.h>
#include "node.h"
#define N 10

int main(void){
    struct node heada, headb;
    int i;
    link t, u, x, a = &heada, b;
    for (i = 0, t = a; i < N; i++){
        t = t->next;
        t->next = NULL;
        t->item = rand()%1000;
    }
    b = &headb;
    b->next = NULL:
    for (t = a->next; t != NULL; t = u){
        u = t->next;
        for (x = b; x->next != NULL: x = x->next)
            if (x->next->item > t->item) 
                break;
        t->next = x->next; 
        x->next = t;
    }
}
