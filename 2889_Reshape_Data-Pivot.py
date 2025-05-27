import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    """
    Pivot the DataFrame to have 'date' as index and 'city' as columns, with 'temperature' as values.
    
    Parameters:
    weather (pd.DataFrame): The DataFrame containing weather data.
    
    Returns:
    pd.DataFrame: A new DataFrame that is the pivoted version of the input.
    """
    return weather.pivot(index='month', columns='city', values='temperature')

# Example usage
data = {
    'month': ['Jan', 'Jan', 'Feb', 'Feb', 'Mar', 'Mar'],
    'city': ['New York', 'Los Angeles', 'New York', 'Los Angeles', 'New York', 'Los Angeles'],
    'temperature': [30, 60, 32, 65, 35, 70]
}
df = pd.DataFrame(data)
result = pivotTable(df)
print(result)