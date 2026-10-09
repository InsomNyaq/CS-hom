// #include<stdio.h>
// #include<stdlib.h>
// #include<time.h>

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
//         return NULL;
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
//         return NULL;

//     Node * p = head->next;
//     while(p != head){
//         printf("%d ", p->data);
//         p = p->next;
//     }
    
// }


// int main(){
//     clock_t start, end;
//     start = clock();

//     int n, m;
//     int index = 0;
//     scanf("%d%d", &n,&m);

//     Node * head = initList();
//     if (head == NULL){
//         return 0;
//     }

//     for(int i = 0; i<n; ++i){
//         int value = 0;
//         insert(head,scanf("%d",&value));
//     }

//     Node * p = head;
//     Node * c = head->next;
//     while(index < m){
//         p = p->next; //current p points to num node m
//         index++;
//     }

//     head->next = p;
    




//     end = clock();
//     double time_used = (double)(end - start) / CLOCKS_PER_SEC;
//     printf("\n%f s\n", time_used);
//     return 0;
// }


#include<stdio.h>
#include<stdlib.h>
#include<time.h>

void reverse(int a[], int left, int right){
    while(left < right){
        int temp = a[left];
        a[left] = a[right];
        a[right] = temp;
        left++; right--;
    }
    
}

int main(){
    // clock_t start, end;
    // start = clock();

    int n, m;
    scanf("%d %d",&n,&m);
    m%=n;
    int a[n];
    for (int i = 0; i<n; ++i){
        scanf("%d", &a[i]);
    }

    int left = 0;
    int right = n-1;
    reverse(a,left,right);

    int left_1 = 0;
    int right_1 = m-1;

    reverse(a, left_1, right_1);
    reverse(a, right_1+1, right);
    for(int i = 0; i<n; ++i){
        if (i > 0) printf(" ");
        printf("%d", a[i]);
    }
    printf("\n");


    // end = clock();
    // double used_time= (double)(end - start) / CLOCKS_PER_SEC;
    // printf("\n%fs\n",used_time);
    return 0;
}