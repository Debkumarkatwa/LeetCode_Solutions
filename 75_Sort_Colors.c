void sortColors(int* nums, int numsSize) {
    int a[] = {0, 0, 0};

    for(int i= 0; i < numsSize; i++){
        if(nums[i] == 0){
            a[0]++;
        }
        else if(nums[i] == 1){
            a[1]++;
        }
        else{
            a[2]++;
        }
    }

    int index = 0;
    for(int i = 0; i < a[0]; i++){
        nums[index++] = 0;
    }
    for(int i = 0; i < a[1]; i++){
        nums[index++] = 1;
    }
    for(int i = 0; i < a[2]; i++){
        nums[index++] = 2;
    }
}

int main() {
    int nums[] = {2, 0, 2, 1, 1, 0};
    int numsSize = sizeof(nums) / sizeof(nums[0]);

    sortColors(nums, numsSize);

    for(int i = 0; i < numsSize; i++) {
        printf("%d ", nums[i]);
    }
    return 0;
}