# include<stdio.h>
# include<stdlib.h>

int trap(int* height, int heightSize) {
    int left = 0, right = heightSize - 1;
    int left_max = 0, right_max = 0;
    int total_water = 0;

    while (left < right) {
        if (height[left] < height[right]) {
            if (height[left] >= left_max) {
                left_max = height[left];
            } else {
                total_water += left_max - height[left];
            }
            left++;
        } else {
            if (height[right] >= right_max) {
                right_max = height[right];
            } else {
                total_water += right_max - height[right];
            }
            right--;
        }
    }

    return total_water;    
}

int main() {
    int arr[] = {0,1,0,2,1,0,1,3,2,1,2,1};
    int size = sizeof(arr)/sizeof(arr[0]);
    int result = trap(arr, size);
    printf("Trapped water: %d\n", result); // Expected output: 6
    return 0;
}