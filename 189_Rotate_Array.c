#include <stdio.h>
#include <stdlib.h>

void rotate(int* nums, int numsSize, int k) {
    int temp, start = 0, end = numsSize - 1;

    if (numsSize == 0 || k <= 0 ) {
        return;
    }
    k = k % numsSize; // Handle cases where k is greater than numsSize

    while (start < end) {
        temp = nums[start];
        nums[start] = nums[end];
        nums[end] = temp;
        start++;
        end--;
    }

    end = k-1, start = 0;
    while (start < end) {
        temp = nums[start];
        nums[start] = nums[end];
        nums[end] = temp;
        start++;
        end--;
    }   

    end = numsSize - 1;
    while (k < end) {
        temp = nums[k];
        nums[k] = nums[end];
        nums[end] = temp;
        k++;
        end--;
    }
}


int main() {
    int nums[] = {1, 2, 3, 4, 5, 6, 7};
    int k = 3;
    int numsSize = sizeof(nums) / sizeof(nums[0]);

    rotate(nums, numsSize, k);

    for (int i = 0; i < numsSize; i++) {
        printf("%d ", nums[i]);
    }
    printf("\n");

    return 0;
}