#include<stdio.h>
#include<stdlib.h>

typedef struct Node{
    int data;
    struct Node *next;
} Node;

Node* reverseList(Node* head){
    Node *pre = NULL;
    Node *cur = head;
    Node *next = NULL;

    while (cur != NULL){
        next = cur->next;
        cur->next = pre;
        pre = cur;
        cur = next;
    }

    return pre;
}

int main(){
    int n = 0;
    scanf("%d", &n);

    Node *head = NULL;
    Node *tail = NULL;
    for (int i = 0; i < n;i++){
        int value = 0;
        scanf("%d", &value);

        Node *node = malloc(sizeof(Node));
        node->data = value;
        node->next = NULL;

        if(head == NULL){
            head = tail = node;
        }else{
            tail->next = node;
            tail = node;
        }
    }

    Node* rehead = reverseList(head);
    Node *c = rehead;
    while(c != NULL){
        
        printf("%d ", c->data);
        c = c->next;
    }
    return 0;
}