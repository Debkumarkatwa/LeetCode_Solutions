#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int* sumZero(int n, int* returnSize) {
    int* result = (int*)malloc(n * sizeof(int));
    int index = 0;

    for (int num = 1; num <= n / 2; num++) {
        result[index++] = -num;
        result[index++] = num;
    }

    if (n % 2 != 0) {
        result[index++] = 0;
    }

    *returnSize = n;
    return result;
    
}

int main() {
    int returnSize;
    int* result = sumZero(5, &returnSize);

    for (int i = 0; i < returnSize; i++) {
        printf("%d ", result[i]);
    }

    printf("\n");
    free(result);
    
    return 0;
}