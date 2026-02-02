#include <stdlib.h>
#include "node.h"

link copy (link t){
    link t1 = malloc(sizeof *t1), l=t1;
    t1->item = t->item;
    while (t->next != t){
        t = t->next;
        t1->next = malloc(sizeof *t1);
        t1 = t1->next;
        t1->item = t->item;
    }
    t1->next = t1;
    return l;
}
