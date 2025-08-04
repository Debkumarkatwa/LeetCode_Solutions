/*
Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).
*/

#include <stdio.h>

double myPow(double x, long n) {
    if (n == 0) return 1; // Base case: x^0 = 1
    if (n < 0) { // If n is negative, calculate the positive power and take reciprocal
        x = 1 / x;
        n = -n;
    }
    
    double result = 1.0;
    while (n > 0) {
        if (n % 2 == 1) { // If n is odd, multiply result by x
            result *= x;
        }
        x *= x; // Square x
        n /= 2; // Divide n by 2
    }
    
    return result;
}

int main() {
    double x = 2.0;
    int n = 3;
    
    double result = myPow(x, n);
    
    printf("Result of %.2f raised to the power of %d is: %.2f\n", x, n, result);
    
    return 0;
}