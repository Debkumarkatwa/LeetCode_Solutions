/*
    Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

    The algorithm for myAtoi(string s) is as follows:
        Whitespace: Ignore any leading whitespace (" ").
        Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
        Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
        Rounding: If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1], then round the integer to remain in the range. Specifically, integers less than -2^31 should be rounded to -2^31, and integers greater than 2^31 - 1 should be rounded to 2^31 - 1.
    
    Return the integer as the final result.
*/

# include <stdio.h>
# include <stdlib.h>

int myAtoi(char* s) {
    int i = 0, sign = 1;
    long result = 0;

    // Skip leading whitespace
    while (s[i] == ' ') {
        i++;
    }

    // Check for sign
    if (s[i] == '-' || s[i] == '+') {
        if (s[i] == '-') {
            sign = -1;
        }
        i++;
    }

    // Convert digits and handle overflow/underflow
    while (s[i] >= '0' && s[i] <= '9') {
        result = result * 10 + (s[i] - '0');
        if (sign == 1 && result > 2147483647) {
            return 2147483647;
        }
        if (sign == -1 && -result < -2147483648) {
            return -2147483648;
        }
        i++;
    }

    return (int)(sign * result);
}

int main() {
    char str1[] = "42";
    char str2[] = "   -42";
    char str3[] = "419 with words";
    char str4[] = "words and 987";
    char str5[] = "-91283472332"; // Out of range
    char str6[] = "2147483648"; // Out of range

    printf("Result for '%s': %d\n", str1, myAtoi(str1)); // Expected: 42
    printf("Result for '%s': %d\n", str2, myAtoi(str2)); // Expected: -42
    printf("Result for '%s': %d\n", str3, myAtoi(str3)); // Expected: 419
    printf("Result for '%s': %d\n", str4, myAtoi(str4)); // Expected: 0
    printf("Result for '%s': %d\n", str5, myAtoi(str5)); // Expected: -2147483648
    printf("Result for '%s': %d\n", str6, myAtoi(str6)); // Expected: 2147483647

    return 0;
}