#include <stdlib.h>
#include <stdbool.h>
#include "node.h"

void delete(link t){
    link u=t;
    while(u->next!=u){
        u=t->next;
        free(t);
    }
    free(u);
}

void delete_even (link t){
    link u;
    while (t->next->next!=t->next){
        u = t->next;
        t->next=t->next->next;
        free(u);
        t=t->next;
    }
}
