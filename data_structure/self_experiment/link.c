#include<stdio.h>
#include<stdlib.h>

typedef struct Node{
    int data;
    struct Node *next;
}Node;

int main(){
    Node *head = NULL;

    Node *node1 = malloc(sizeof(Node));
    Node *node2 = malloc(sizeof(Node));
    Node *node3 = malloc(sizeof(Node));

    node1->data = 10;
    node2->data = 20;
    node3->data = 30;

    node1->next = node2;
    node2->next = node3;
    node3->next = NULL;

    head = node1;

    Node *cur = head;

    while(cur != NULL){
        printf("%d\n", cur->data);
        cur = cur->next;
    }

    free(node1);
    free(node2);
    free(node3);
    return 0;
}