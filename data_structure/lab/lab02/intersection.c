#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node *next;
} Node;

// 创建新节点
Node *createNode(int data) {
    Node *p = (Node *)malloc(sizeof(Node));
    p->data = data;
    p->next = NULL;
    return p;
}

// 读取链表，遇到 -1 结束
Node *createList() {
    Node *head = createNode(0);
    Node *tail = head;
    int x;

    while (scanf("%d", &x) == 1 && x != -1) {
        tail->next = createNode(x);
        tail = tail->next;
    }

    Node *first = head->next;
    free(head);
    return first;
}

// 求两个有序链表的交集
Node *intersection(Node *L1, Node *L2) {
    Node *head = createNode(0);
    Node *tail = head;

    while (L1 != NULL && L2 != NULL) {
        if (L1->data < L2->data) {
            L1 = L1->next;
        } else if (L1->data > L2->data) {
            L2 = L2->next;
        } else {
            tail->next = createNode(L1->data);
            tail = tail->next;

            L1 = L1->next;
            L2 = L2->next;
        }
    }

    Node *result = head->next;
    free(head);
    return result;
}

int main() {
    Node *L1 = createList();
    Node *L2 = createList();

    Node *L3 = intersection(L1, L2);

    if (L3 == NULL) {
        printf("NULL");
    } else {
        Node *p = L3;
        int first = 1;

        while (p != NULL) {
            if (!first) {
                printf(" ");
            }
            printf("%d", p->data);
            first = 0;
            p = p->next;
        }
    }

    printf("\n");
    return 0;
}