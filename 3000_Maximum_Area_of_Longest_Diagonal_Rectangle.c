#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int areaOfMaxDiagonal(int** dimensions, int dimensionsSize, int* dimensionsColSize) {
    int maxdia = 0, maxarea = 0;
    for (int i = 0; i < dimensionsSize; i++){
        int l = dimensions[i][0], w = dimensions[i][1];

        int diaSq = l * l + w * w;
        if (diaSq > maxdia){
            maxdia = diaSq;
            maxarea = l * w;
        }
        else if (diaSq == maxdia){
            maxarea = (l*w > maxarea)? l*w : maxarea;
        }
    }
    
    return maxarea;
}

int main() {
    int dimensionsSize = 3;
    int* dimensionsColSize = (int[]){2, 2, 2};
    int** dimensions = (int**)malloc(dimensionsSize * sizeof(int*));
    for (int i = 0; i < dimensionsSize; i++) {
        dimensions[i] = (int*)malloc(dimensionsColSize[i] * sizeof(int));
    }

    // Example input: [[4,5],[2,3],[4,3]]
    dimensions[0][0] = 4; dimensions[0][1] = 5;
    dimensions[1][0] = 2; dimensions[1][1] = 3;
    dimensions[2][0] = 4; dimensions[2][1] = 3;

    int result = areaOfMaxDiagonal(dimensions, dimensionsSize, dimensionsColSize);
    printf("Area of the rectangle with the maximum diagonal: %d\n", result);

    for (int i = 0; i < dimensionsSize; i++) {
        free(dimensions[i]);
    }
    free(dimensions);

    return 0;

}