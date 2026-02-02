#ifndef NODE_H_
#define NODE_H_

typedef int Item;
typedef struct node *link;
struct node{
    Item item;
    link next;
};
#endif
