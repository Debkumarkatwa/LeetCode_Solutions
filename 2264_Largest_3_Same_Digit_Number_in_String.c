# include<stdio.h>
# include<string.h>
# include<stdlib.h>

char* largestGoodInteger(char* num) {
    int n = strlen(num);
    char* result = (char*)malloc(4 * sizeof(char));
    result[0] = '\0'; // Initialize result as an empty string

    for (int i = 0; i < n - 2; i++) {
        if (num[i] == num[i + 1] && num[i] == num[i + 2]) {
            // Found a triplet of the same digit
            if (result[0] == '\0' || num[i] > result[0]) {
                result[0] = num[i];
                result[1] = num[i];
                result[2] = num[i];
                result[3] = '\0'; // Null-terminate the string
            }
        }
    }

    // If no triplet found, return an empty string
    if (result[0] == '\0') {
        free(result);
        return "";
    }

    return result;
    
}

int main() {
    char num[100];
    printf("Enter the number string: ");
    scanf("%s", num);
    
    char* result = largestGoodInteger(num);
    printf("%s\n", result);
    
    return 0;
}