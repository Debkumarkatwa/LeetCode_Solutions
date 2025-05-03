# include<stdio.h>

int maxArea(int* height, int heightSize) {
    int left = 0, right = heightSize - 1;
    // int chosen_left = 0, chosen_right = 0;  // if want to track the container
    int max_area = 0;
    
    while (left < right) {
        int width = right - left;
        int min_height = height[left] < height[right] ? height[left] : height[right];
        int area = width * min_height;

        if (area > max_area) {
            max_area = area;
            // chosen_left = left;  // update the chosen left index
            // chosen_right = right;  // update the chosen right index
        }

        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }

    // printf(" Chosen left index: %d, height: %d\n Chosen right index: %d, height: %d\n", chosen_left, height[chosen_left], chosen_right, height[chosen_right]);
    return max_area;  
}

int main() {
    int height[] = {1,8,6,2,5,4,8,3,7};
    int heightSize = sizeof(height) / sizeof(height[0]);

    int result = maxArea(height, heightSize);
    printf("The maximum area is: %d\n", result);

    return 0;
}