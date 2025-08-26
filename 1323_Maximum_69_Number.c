# include <stdio.h>
# include <string.h>

int maximum69Number (int num) {
    int reverse = 0;
    int track = 1;
    
    while (num > 0) {
        int digit = num % 10;
        reverse = reverse * 10 + digit;
        num /= 10;
    }

    while (reverse > 0 ) {
        int digit = reverse % 10;
        if (digit == 6 && track) {
            digit = 9; // Change the first '6' to '9'
            track = 0; // Only change the first occurrence
        }
        num = num * 10 + digit;
        reverse /= 10;
    }

    return num;
    
}

int maximum69Number (int num) {
    char str[12]; // Enough to hold 32-bit integer
    sprintf(str, "%d", num); // Convert integer to string

    for (int i = 0; str[i] != '\0'; i++) {
        if (str[i] == '6') {
            str[i] = '9'; // Change the first '6' to '9'
            break; // Only change the first occurrence
        }
    }

    return atoi(str); // Convert back to integer
    
}

int main() {
    int num[] = {9669,6669,9999,9996};

    for (int i = 0; i < sizeof(num)/sizeof(num[0]); i++) {
        int result = maximum69Number(num[i]);
        printf("Maximum 69 Number for %d: %d\n", num[i], result);
    }
    return 0;
}