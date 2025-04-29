# include<stdio.h>    // Using "Moore's Voting Algorithm" to find the majority element in an array

int majorityElement(int* nums, int numsSize) {
    int answer = 0, freq = 0;

    for (int i = 0; i < numsSize; i++){
        if (freq == 0){
            answer = nums[i];
            freq = 1;
        } else if (nums[i] == answer){
            freq++;
        } else {
            freq--;
        }
    }

    return answer;    
}

int main(){
    int nums[] = {2,2,1,1,1,2,2};
    int numsSize = sizeof(nums)/sizeof(nums[0]);

    printf("%d\n", majorityElement(nums, numsSize));

    return 0;
}