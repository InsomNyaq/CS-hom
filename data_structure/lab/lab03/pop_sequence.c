#include<stdio.h>
#include<stdlib.h>

#define MAXSIZE 1000

typedef struct {
    int data[MAXSIZE];
    int top;
}stack;

void initStock(stack * s){
    s->top=-1;
}

//weather empty or not
int isEmpty(stack * s){
    return s->top == -1;
}

//full or not
int isFull(stack * s, int m){
    return s->top == m-1;
}

//into stack:return 1 if successed else 0
int PushELE(stack * s, int x, int m){
    if(isFull(s,m)) return 0;
    s->data[++s->top] = x;
    return 1;
}
// pop the top element in stack,  failed: 0
int PopELE(stack * s, int *x){
    if(isEmpty(s)) return 0;
    *x = s->data[s->top--];
    return 1;
}

//get the top ele instead of pop
int GetTop(stack * s, int *x){
    if (isEmpty(s)) return 0;
    *x = s->data[s->top];
    return 1;
}

//check the pop sequence
int isPopSequence(int m, int n, int popSeq[]){
    stack s;
    initStock(&s);
    int nextPush = 1;

    for(int i = 0; i<n; ++i){
        int target = popSeq[i];
        int topValue;

        while(1){
            if(GetTop(&s, &topValue) && topValue == target) break;
            if(nextPush > n) return 0;
            if(!PushELE(&s,nextPush,m)) return 0;

            nextPush++;
        }
        PopELE(&s, &topValue);
    }
    return 1;
}

int main(){
    int m, n, k;
    scanf("%d %d %d",&m, &n, &k);
    int popSeq[MAXSIZE];

    for(int i = 0; i<k; ++i){
        for(int j = 0; j<n; ++j){
            scanf("%d", &popSeq[j]);
        }

        if (isPopSequence(m, n, popSeq)){
            printf("\nYES");
        }else{
            printf("\nNO");
        }
    }
    return 0;
}