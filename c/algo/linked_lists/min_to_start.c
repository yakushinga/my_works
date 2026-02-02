#include "node.h"

void min_to_start (link t){
    link min = t, x = t, l;
    do{
        if (x->next->item < min->next->item)
            min = x;
        x=x->next;
    } while(x->next != x);
    l = min->next->next;
    Item a = t->item, b;
    t->item = min->next->item;
    t = t->next;
    while (t != l){
        b = t->item;
        t->item = a;
        a = b;
        t=t->next;
    }
}
