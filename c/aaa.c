// Online C compiler to run C program online
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int a; 
    struct Task *p; 
    int arr[100]; 
    
} Task; 

int main() {
    // Write C code here
    // printf("Try programiz.pro");
    printf("%d\n", sizeof(long)); 
    int arr[100]; 
    arr[2] = 1; 
    int *p = (int *)0x7ffc36ddd000; 
    // printf("%d\n", *p); 
    // printf("%d\n", sizeof(int)); 
    // for(int i = 0; i < 5; i++) {
    //     printf("%d, %p\n", *p, p); 
    //     p += 1; // sizeof(int); 
    // }

    Task x; 
    printf("%d\n", x.a); 
    Task *px = (Task *)malloc(sizeof(Task)); 
    printf("%d\n", px -> a); 
    printf("%d\n", sizeof(x)); 
    
        
    return 0;
}