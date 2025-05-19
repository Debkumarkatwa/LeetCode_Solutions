# include<stdio.h>
int arithmeticTriplets(int* nums, int numsSize, int diff) {
    int count = 0;
    
    for(int i = 0; i < numsSize; i++){
        int second = 0, third = 0;

        for(int j = i + 1; j < numsSize; j++){
            if(nums[j] - nums[i] == diff){
                second = 1;
            }
            if(nums[j] - nums[i] == 2 * diff){
                third = 1;
            }

            if(second && third){
                count++;
                break; // No need to check further for this i as all values are unique
            }
        }
    }

    return count;
}