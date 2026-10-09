#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

bool check_sort(int a[], int n){
    for(int i=0; i<n-1; i++){
        if (a[i] >= a[i+1]){
            printf("Invalid Value");
            return false;
        }
    }
    return true;
}
void Print_process(int left, int right, int mid){
    printf("[%d,%d][%d]\n", left,right,mid);
}

int main(){
    int n, x;
    if (scanf("%d", &n) != 1) {
    return 1;
    }

    if (scanf("%d", &x) != 1) {
        return 1;
    }

    if (n <= 0) {
        return 1;
    }

    int array[n];

    for (int i = 0; i < n; i++) {
        if (scanf("%d", &array[i]) != 1) {
            return 1;
        }
    }

    if(!check_sort(array, n))
    {
        return 1;
    }
    

    int left = 0;
    int right = n-1;
    bool found = false;
    while(left <= right){
        int mid = (left + right) / 2;
        Print_process(left, right, mid);
        if(array[mid] == x){
            printf("%d",mid);
            found = true;
            break;
        }

        if (array[mid] < x){
            left = mid + 1;
        }
        else if(array[mid] > x){
            right = mid - 1;
        }
    }
    if (!found){
        printf("Not Found");
    }
    return 0;
}