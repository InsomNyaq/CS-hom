// #include<stdio.h>
// #include<stdlib.h>

// typedef struct Node{
//     int data;
//      struct Node * next;
// }Node;

// Node* initList(){
//     Node * head = (Node*)malloc(sizeof(Node));

//     if(head == NULL){
//         return NULL;
//     }

//     head->next = head;
//     return head;
// }

// //tail insert
// void insert(Node * head, int value){
//     Node * node=(Node*)malloc(sizeof(Node));

//     if (node == NULL){
//         return;
//     }

//     node->data = value;
//     Node * p = head;

//     while(p != head){
//         p = p ->next;
//     }

//     node->next = head;
//     p ->next = node;
// }

// void destroyList(Node * head){
//     if(head == NULL)
//         return;
    
//     Node *p = head->next;

//     while(p != head){
//         Node * temp = p;
//         p = p->next;
//         free(temp);
//     }

//     free(head);
// }

// //print the eles in the list
// void printList(Node* head){
//     if(head == NULL)
//         return;

//     Node * p = head->next;
//     while(p != head){
//         printf("%d ", p->data);
//         p = p->next;
//     }
    
// }

// int main(){
//     int nums, key;
//     Node * head = initList();
//     Node * p = head->next;
//     Node * p_1 = p->next;
//     scanf("%d", &nums);
//     for (int i = 0; i<nums; i++){
//         int value = 0;
//         scanf("%d",&value);
//         insert(head,value);
//     }
//     scanf("%d",&key);

//     Node * key_node = (Node *)malloc(sizeof(Node));
//     key_node->data = key;


//     while(p != head){
//         if(p_1->data < key && p->data < key ){
//             p = p->next;
//             p_1 = p->next;
//         }else{
//             p->next = key_node;
//             key_node->next = p_1;
//             break;
//         }
//     }
//     printList(head);
    
//     destroyList(head);
//     free(key_node);
//     return 0;
// }

#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node *next;
} Node;

Node* initList() {
    Node *head = (Node*)malloc(sizeof(Node));
    if (head == NULL) {
        return NULL;
    }
    head->next = head; // 循环链表，头结点指向自己
    return head;
}

// 尾插法
void insert(Node *head, int value) {
    Node *node = (Node*)malloc(sizeof(Node));
    if (node == NULL) {
        return; // void 函数直接返回
    }

    node->data = value;
    Node *p = head;

    // 寻找尾结点（p->next 指向 head 的结点）
    while (p->next != head) {
        p = p->next;
    }

    node->next = head;
    p->next = node;
}

void destroyList(Node *head) {
    if (head == NULL)
        return;
    
    Node *p = head->next;
    while (p != head) {
        Node *temp = p;
        p = p->next;
        free(temp);
    }
    free(head);
}

// 打印链表元素
void printList(Node *head) {
    if (head == NULL)
        return;

    Node *p = head->next;
    while (p != head) {
        printf(" ");
        printf("%d", p->data);
        p = p->next;
    }
    printf("\n");
}

int main() {
    int nums, key;
    Node *head = initList();
    
    scanf("%d", &nums);
    for (int i = 0; i < nums; i++) {
        int value = 0;
        scanf("%d", &value);
        insert(head, value); // 修正 scanf 传参
    }
    scanf("%d", &key);

    // 为 key 创建新结点并分配内存
    Node *key_node = (Node*)malloc(sizeof(Node));
    key_node->data = key;

    // 链表构建完成后，再初始化遍历指针
    Node *p = head;       // 从 head 开始
    Node *p_1 = head->next; // 第一个真实数据结点

    // 寻找插入位置并插入
    while (p_1 != head && p_1->data < key) {
        p = p_1;
        p_1 = p_1->next;
    }

    // 将 key_node 插入到 p 和 p_1 之间
    key_node->next = p_1;
    p->next = key_node;

    printList(head);
    destroyList(head);
    
    return 0;
}
