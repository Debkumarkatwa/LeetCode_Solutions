/*
    Given an integer x, return true if x is a palindrome, and false otherwise.
*/

# include<stdio.h>
# include<stdbool.h>

bool isPalindrome(int x) {
    int copy = x, reverse = 0, reminder;
    while (x){
        reminder = x % 10;
        reverse = reverse * 10 + reminder;
        x /= 10; 
    }

    if (copy == reverse){
        return 1;
    }
    return 0;
}

int main() {
    int test1 = 121;
    int test2 = -121;
    int test3 = 10;
    int test4 = 12321;

    printf("Is %d a palindrome? %s\n", test1, isPalindrome(test1) ? "true" : "false"); // Expected: true
    printf("Is %d a palindrome? %s\n", test2, isPalindrome(test2) ? "true" : "false"); // Expected: false
    printf("Is %d a palindrome? %s\n", test3, isPalindrome(test3) ? "true" : "false"); // Expected: false
    printf("Is %d a palindrome? %s\n", test4, isPalindrome(test4) ? "true" : "false"); // Expected: true

    return 0;
}