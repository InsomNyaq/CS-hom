#include<stdio.h>
#include<stdlib.h>
#define MAX_VALUE 1001L
int a[MAX_VALUE];

void insert_sorted(int a[], int n, int key){
   int i = n-1;
   
   while(i >= 0 && a[i] > key){
    a[i+1] = a[i];
    i--;
   }
    a[i+1] = key;  
}

int main(){
    long int n;
    int key = 0;
    scanf("%ld",&n);

    for(int i = 0; i<n; ++i){
        scanf("%d", &a[i]);
    }
    scanf("%d", &key);
   
    insert_sorted(a, n, key);


    for(int i = 0; i< n + 1; ++i){
        if(i>0) printf(" ");
        printf("%d", a[i]);
    }
    printf("\n");
    return 0;
}