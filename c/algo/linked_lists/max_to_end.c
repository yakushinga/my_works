#include "node.h"

void print (link t); 
void max_to_end (link t);

#if 0
int main (int argc, char * argv[]){
    int N = atoi(argv[1]);
    link t, x, max;
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
    t=x;
    max_to_end(t);
    return 0;
}
#endif
void max_to_end(link t){
    link max = t, x = t;
    while (t->next->next != t->next){
        if (t->next->item > max->next->item)
            max = t;
        t = t->next;
    }
    t=t->next;
    if (x->item > max->next->item){
        t->next=x;
        x=x->next;
        t->next->next=t->next;
    }
    else{
        t->next = max->next;
        max->next=max->next->next;
        t->next->next=t->next;
    }
    t=x;
}

