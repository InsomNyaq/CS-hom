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

//create a intersection link of L1 and L2
Node * interLink(Node* l1, Node* l2){
    Node * head = malloc(sizeof(Node));
    head->next = NULL;
    Node * tail = head;

    Node * p = l1->next;
    Node * q = l2->next;

    while(p != NULL){
        if (p->data == q->data){
            tail->next = p;
            tail = p;
            q = q->next;
            p = p->next;
        }
        p = p->next;
    }
    tail->next = NULL;
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

void freeLink(Node * head){
    if(head == NULL) return;

    Node * p;
    while(head != NULL){
        p = head;
        head = head ->next;
        free(p);
    }
}

int main(){
    Node * s1 = createLink();
    Node * s2 = createLink();

    Node * s3 = interLink(s1, s2);
    printLink(s3);
    
    freeLink(s3);

    return 0;
}