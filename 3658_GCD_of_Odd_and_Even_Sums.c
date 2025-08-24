#include <stdio.h>

int gcdOfOddEvenSums(int n) {
    int sumOdd = 0, sumEven = 0;

    for(int i = 1; i <= n*2; i++){
        if(i % 2 == 0)
            sumEven += i;
        else
            sumOdd += i;
    }

    int temp;
    while (sumOdd != 0) {
        temp = sumOdd;
        sumOdd = sumEven % sumOdd;
        sumEven = temp;
    }

    return sumEven;
}

int main() {
    int n;
    printf("Enter a positive integer n: ");
    scanf("%d", &n);
    
    int result = gcdOfOddEvenSums(n);
    printf("GCD of sums of odd and even integers from 1 to %d is: %d\n", n * 2, result);
    
    return 0;
}