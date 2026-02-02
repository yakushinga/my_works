#include "node.h"
#include <stdbool.h>

bool in_one_circle (link t, link u){
    while (t->next != t){
        if (t == u)
            return true;
        t=t->next;
    }
    return false;
}
