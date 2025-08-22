#include<stdio.h>
#include<stdlib.h>

int missingNumber(int* nums, int numsSize) {
    int mis_num = 0;
    for (int i = 0; i < numsSize; i++) {
        mis_num ^= (i + 1) ^ nums[i];
    }

    return mis_num;
}

int main() {
    int nums[] = {3, 0, 1, 2};
    int numsSize = sizeof(nums) / sizeof(nums[0]);

    int missing = missingNumber(nums, numsSize);
    printf("Missing number: %d\n", missing);

    return 0;
}

