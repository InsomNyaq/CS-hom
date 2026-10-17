#include<stdlib.h>
#include<stdio.h>

typedef struct Node{
    int data;
    struct Node *next;
}Node;

Node* mergeLink(Node * head_1, Node* head_2,Node *head_3){
    Node *p_1 = head_1;
    Node *p_2 = head_2;
    Node *p_3 = head_3;

    while(head_1 != NULL && head_2 != NULL){
        Node *node = malloc(sizeof(Node));
        node->data = p_1->data > p_2->data ? p_1->data : p_2->data;
        node->next = NULL;
        p_3->next = node;
        p_3 = node;
    }
}

int main(){
    
    return 0;
}