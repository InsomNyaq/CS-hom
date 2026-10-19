#include<stdio.h>
#include<stdlib.h>

typedef struct Node{
    int data;
    struct Node * next;
}Node;

//create a link
Node * createLink(){
    Node * head = malloc(sizeof(Node));
    head->next = NULL;
    Node * tail = head;
    int x;

    while(scanf("%d", &x) == 1 && x != -1){
        Node * p = malloc(sizeof(Node));
        p->data = x;
        p->next = NULL;

        tail->next = p;
        tail = p;
    }

    return head;
}

//merge two links
Node * mergeLink(Node* L1, Node* L2){
    Node * p = L1->next;
    Node * q = L2->next;

    Node * head = malloc(sizeof(Node));
    head->next = NULL;
    Node * tail = head;
    
    while(p != NULL && q !=NULL){
        if(p->data <= q->data){
            tail->next = p;
            p = p->next;
        }else{
            tail->next = q;
            q = q->next;
        }

        tail = tail->next;
    }

    if (p != NULL){
        tail->next = p;
    }else{
        tail->next = q;
    }

    return head;
}

//print the link_merged
void printLink(Node * L){
    Node * p = L->next;
    if(p == NULL){
        printf("NULL\n");
        return;
    }

    int first = 1;
    while(p)
    {
     if (!first){
        printf(" ");
    }

    printf("%d", p->data);
    p = p->next;
    first = 0;
    }
    printf("\n");
}

int main(){


    return 0;
}