#ifndef STACK_ARRAY_H
#define STACK_ARRAY_H

#include <stdlib.h>
#include "stack.h"

static Item *s;
static int N;
void STACKinit(int maxN){
    s = malloc(maxN * sizeof(Item));
    N = 0;
}

int STACKempty (void){
    return N == 0;
}

void STACKpush(Item item){
    s[N++] = item;
}

Item STACKpop(void){
    return s[--N];
}

#endif
