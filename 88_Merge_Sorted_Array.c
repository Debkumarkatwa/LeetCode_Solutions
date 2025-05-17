# include <stdio.h>

void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n) {
    m = m - 1, n = n - 1;
    int k = nums1Size - 1;
    
    // Merge in reverse order to avoid overwriting nums1
    while (m >= 0 && n >= 0) {
        if (nums1[m] > nums2[n]) {
            nums1[k--] = nums1[m--];
        } else {
            nums1[k--] = nums2[n--];
        }
    }
    // Copy remaining elements from nums2 if any
    while (n >= 0) {
        nums1[k--] = nums2[n--];
    }
}

int main() {
    int nums1[6] = {1, 2, 3, 0, 0, 0};
    int nums2[3] = {2, 5, 6};
    int m = 3;
    int n = 3;
    
    merge(nums1, sizeof(nums1)/sizeof(int), 3, nums2, sizeof(nums2)/sizeof(int), 3);
    
    for (int i = 0; i < m + n; i++) {
        printf("%d ", nums1[i]);
    }
    
    return 0;
}