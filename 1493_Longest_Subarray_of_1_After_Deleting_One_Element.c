#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int longestSubarray(int* nums, int numsSize) {
    int maxLength = 0;
    int left = 0, right = 0, temp_left = 0;
    int zeroCount = 0;
    
    for (right = 0; right < numsSize; right++) {
        if (nums[right] == 0){
            zeroCount++;

            if (zeroCount == 2){
                maxLength = (right - left - 1 > maxLength) ? right - left - 1 : maxLength;
                left = temp_left + 1;
                zeroCount = 1;
            }

            temp_left = right;
        }
    }
    maxLength = (right - left - 1 > maxLength) ? right - left - 1 : maxLength;

    return maxLength;
}

int main() {
    int nums[] = {1, 1, 1};
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    int result = longestSubarray(nums, numsSize);
    printf("Length of the longest subarray: %d\n", result);
    return 0;
}
