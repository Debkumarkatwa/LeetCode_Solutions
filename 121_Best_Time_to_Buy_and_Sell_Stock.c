# include<stdio.h>

int MaxProfit(int arr[], int size){
    
    int max_profit = 0, min_price = arr[0];
    int buy_day = 0, sell_day = 0, temp_buy_day = 0;   // OPTIONAL : Initialize buy and sell days : OPTIONAL

    for(int i = 1; i < size; i++){
        if(arr[i] > min_price){
            int profit = arr[i] - min_price;
            if(profit > max_profit){
                max_profit = profit;
                sell_day = i; // OPTIONAL : Update sell day  
                buy_day = temp_buy_day; // OPTIONAL : Update buy day based on the last potential buy day
            }
        }
        // Update min_price if current price is less than min_price
        if(arr[i] < min_price){
            min_price = arr[i];
            temp_buy_day = i; // OPTIONAL : Update potential buy day
        }
    }

    // printf("Buy on day %d at price %d, Sell on day %d at price %d\n", buy_day + 1, arr[buy_day], sell_day + 1, arr[sell_day]);
    
    return max_profit;
}

int main(){

    int arr[] = {2,1,4};
    int size = sizeof(arr)/sizeof(arr[0]);

    int maxProfit = MaxProfit(arr, size);
    printf("Max Profit: %d\n", maxProfit);

    return 0;
}