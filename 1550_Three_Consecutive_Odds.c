#include <stdbool.h>
#include <stdio.h>
bool threeConsecutiveOdds(int* arr, int arrSize) {
    int count = 0;
    for(int i = 0; i < arrSize; i++){
        if(arr[i] % 2 != 0){
            count++;
        }
        else{
            count = false;
        }

        if(count == 3){
            return true;
        }
    }

    return 0;
}

int main() {
    int arr[] = {1, 2, 3, 4, 5, 7, 9};
    int arrSize = sizeof(arr) / sizeof(arr[0]);
    bool result = threeConsecutiveOdds(arr, arrSize);
    printf("%s\n", result ? "true" : "false");
    return 0;
}