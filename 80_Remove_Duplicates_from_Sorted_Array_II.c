# include <stdio.h>
# include <stdlib.h>

int removeDuplicates(int* nums, int numsSize) {
    int uniqueCount = 1, count = 1;
    if (numsSize == 0) return 0;
    
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] == nums[i-1]){
            count++;
        }
        else {
            count = 1;
        }

        if (count > 2) {
            continue;
        }
        uniqueCount++;
        nums[uniqueCount - 1] = nums[i];
    }

    return uniqueCount;
}

int main() {
    int nums[] = {1,1,1,2,2,3};
    int size = sizeof(nums) / sizeof(nums[0]);
    
    int newSize = removeDuplicates(nums, size);
    
    printf("New size: %d\n", newSize);
    printf("Array after removing duplicates: ");
    for (int i = 0; i < newSize; i++) {
        printf("%d ", nums[i]);
    }
    printf("\n");
    
    return 0;
}