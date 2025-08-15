#include<stdio.h>
#include<stdbool.h>

bool isPowerOfFour(int n) {
    if (n <= 0) {
        return false;
    }
    
    while (n % 4 == 0) {
        n /= 4;
    }

    return n == 1;
}

int main() {
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    
    if (isPowerOfFour(n)) {
        printf("%d is a power of four.\n", n);
    } else {
        printf("%d is not a power of four.\n", n);
    }
    
    return 0;
}