#include "node.h"

void swap_nodes (link t, link u){
    link a = u->next->next;

    u->next->next = t->next->next;
    t->next->next = a;
    
    link b = u->next;

    u->next = t->next;
    t->next = b;
}
