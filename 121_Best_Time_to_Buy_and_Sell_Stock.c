# include<stdio.h>

int MaxProfit(int arr[], int size){
    
    int max_profit = 0, min_price = arr[0];

    for(int i = 1; i < size; i++){
        if(arr[i] > min_price){
            int profit = arr[i] - min_price;
            if(profit > max_profit){
                max_profit = profit;
            }
        }// Update min_price if current price is less than min_price
        
        if(arr[i] < min_price){
            min_price = arr[i];
        }
    }
    
    return max_profit;

}

int main(){

    int arr[] = {2,1,4};
    int size = sizeof(arr)/sizeof(arr[0]);

    int maxProfit = MaxProfit(arr, size);
    printf("Max Profit: %d\n", maxProfit);

    return 0;
}