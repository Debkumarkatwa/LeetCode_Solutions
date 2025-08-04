# include <stdio.h>

int maxSubArray(int* nums, int numsSize) {
    int current_sum = 0, max_sum = nums[0];
    int start=0, end=0; // Optional

    for (int i = 0; i < numsSize; i++){
        current_sum += nums[i];

        if (current_sum > max_sum){
            max_sum = current_sum;
            end = i; // Optional
        }

        if (current_sum < 0){
            current_sum = 0;
            start = i + 1; // Optional
        }
    }

    // Optionally, you can print the subarray-------------------------
    // printf("Maximum Subarray: ");
    // for (int i = st; i <= end; i++) {
    //     printf("%d -- ", nums[i]);
    // }

    return max_sum;
}

int main(){
    int nums[] = {3,-4,5,4,-1,7,-8};
    int numsSize = sizeof(nums) / sizeof(nums[0]);

    int result = maxSubArray(nums, numsSize);

    printf("Maximum Subarray Sum: %d\n", result);

    return 0;
    
}