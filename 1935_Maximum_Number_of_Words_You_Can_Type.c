#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int canBeTypedWords(char* text, char* brokenLetters) {
    int count = 0;
    char* word;
    char* rest = text;
    int broken[26] = {0};

    // Mark broken letters
    for (int i = 0; brokenLetters[i] != '\0'; i++) {
        broken[brokenLetters[i] - 'a'] = 1;
    }

    // Split text into words and check each word
    while ((word = strtok_r(rest, " ", &rest))) {
        int canType = 1;
        for (int i = 0; word[i] != '\0'; i++) {
            if (broken[word[i] - 'a']) {
                canType = 0;
                break;
            }
        }
        if (canType) {
            count++;
        }
    }

    return count;
    
}

int main() {
    char text[] = "hello world";
    char brokenLetters[] = "ad";
    int result = canBeTypedWords(text, brokenLetters);
    printf("Result: %d\n", result); // Expected output: 1    

    return 0;
}