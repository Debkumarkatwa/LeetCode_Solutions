# include <stdio.h>

int maxSubArray(int* nums, int numsSize) {
    int current_sum = 0, max_sum = nums[0];

    for (int start = 0; start < numsSize; start++){
        current_sum += nums[start];

        if (current_sum > max_sum){
            max_sum = current_sum;
        }

        if (current_sum < 0){
            current_sum = 0;
        }
    }

    return max_sum;
}

int main(){
    int nums[] = {-2,1,-3,4,-1,2,1,-5,4};
    int numsSize = sizeof(nums) / sizeof(nums[0]);

    int result = maxSubArray(nums, numsSize);

    printf("Maximum Subarray Sum: %d\n", result);

    return 0;
    
}