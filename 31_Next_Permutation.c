# include<stdio.h>
# include<stdlib.h>

void nextPermutation(int* nums, int numsSize) {
    int i = numsSize - 2, j;
    while(i >= 0 && nums[i] >= nums[i + 1]){
        i -= 1;
    }

    if(i >= 0){
        j = numsSize -1;
        
        while(nums[j] <= nums[i]){
            j -= 1;
        }
        
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
    int left = i + 1, right = numsSize - 1;
    while(left < right){
        int temp = nums[left];
        nums[left] = nums[right];
        nums[right] = temp;
        left += 1;
        right -= 1;
    }
    
}

int main(){
    int arr[] = {1, 5, 1};
    int size = sizeof(arr)/sizeof(arr[0]);
    nextPermutation(arr,size);
    for(int i=0;i<size;i++){
        printf("%d ",arr[i]);
    }
    return 0;
}