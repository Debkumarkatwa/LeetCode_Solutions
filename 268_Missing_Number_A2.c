#include<stdio.h>
#include<stdlib.h>

int missingNumber(int* nums, int numsSize) {
    int all_sum = numsSize * (numsSize + 1) / 2;
    int sum = 0;

    for (int i = 0; i < numsSize; i++) {
        sum += nums[i];
    }

    return all_sum - sum;
}

int main() {
    int nums[] = {3, 0, 1, 2};
    int numsSize = sizeof(nums) / sizeof(nums[0]);

    int missing = missingNumber(nums, numsSize);
    printf("Missing number: %d\n", missing);

    return 0;
}