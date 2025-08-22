#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int romanToInt(char* s) {
    
    int result = 0, flag = 0;
    int size = strlen(s);

    int b[size];

    for(int i =0; i < size; i++){
        switch (s[i]){
            case 'I':
                b[i] = 1;
                break;

            case 'V':
                b[i] = 5;
                break;

            case 'X':
                b[i] = 10;
                break;

            case 'L':
                b[i] = 50;
                break;

            case 'C':
                b[i] = 100;
                break;
                
            case 'D':
                b[i] = 500;
                break;
                
            case 'M':
                b[i] = 1000;
                break;
        }
    }
    
    for(int i = 0; i < size; i++){
        if(flag == 1){
                flag = 0;
                continue;
        }

        if(i == size-1){
            result +=b[i];
        }
        else{
            if(b[i] < b[i+1]){
                result += (b[i+1]-b[i]);
                flag = 1;
            }
            else
                result += b[i];
        }
    }

    return result;  
}
 
int main() {
    char num[] = "MCMXCIV";

    int result = romanToInt(num);
    printf("Roman '%s' == '%d' in Number", num, result);
    
    return 0;
}