/*
    Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
    Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
*/

# include<stdio.h>

int reverse(int x){
    int reverse = 0, reminder;
    while (x){
        reminder = x % 10;
        reverse = reverse * 10 + reminder;
        x /= 10; 
    }
    if (reverse > 2147483647 || reverse < - 2147483648){
        return 0;
    }
    return reverse;
}

int main(){
    int x = 123;
    int result = reverse(x);
    printf("Reversed: %d\n", result); // Expected output: 321

    x = -123;
    result = reverse(x);
    printf("Reversed: %d\n", result); // Expected output: -321

    x = 120;
    result = reverse(x);
    printf("Reversed: %d\n", result); // Expected output: 21

    x = 0;
    result = reverse(x);
    printf("Reversed: %d\n", result); // Expected output: 0

    return 0;
}