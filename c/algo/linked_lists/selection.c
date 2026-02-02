#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "node.h"

link selection (link t, bool (*function) (link t)){
    link x = t, u;
    while (!(function(x)) && t->next!=t){
        x = t->next;
        free(t);
        t = x;
    }
    while (t->next != t){
        u = t;
        t = t->next;
        if (t->next == t && !(function(t))){
            u->next = u;
            free(t);
            t = u;
        }
        else if(!(function(t))){
            u->next=u->next->next;
            free(t);
            t = u;
        }
    }
    return x;
}
