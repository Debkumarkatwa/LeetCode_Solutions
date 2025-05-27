import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    """
    Concatenate two DataFrames along the columns.
    
    Parameters:
    df1 (pd.DataFrame): The first DataFrame.
    df2 (pd.DataFrame): The second DataFrame.
    
    Returns:
    pd.DataFrame: A new DataFrame that is the concatenation of df1 and df2.
    """
    return pd.concat([df1, df2], axis=0)

# Example usage
data1 = {'name': ['Tom', 'Jerry'], 'salary': [105, 101]}
data2 = {'name': ['Mickey', 'Minnie'], 'salary': [101, 140]}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
result = concatenateTables(df1, df2)
print(result)