
int search(int* nums, int numsSize, int target) {
    return binary_search(nums, 0, numsSize - 1, target);
}

int binary_search(int* a, int l, int h, int x) {
    if(h>=l){
        int mid=(l+h)/2;
        if(a[mid]==x)
        return mid;
        
        if(a[mid]>x){
            return binary_search(a,l,mid-1,x);
        }
        return binary_search(a,mid+1,h,x);
    }
    return -1;
}
