import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    """
    Select the first 5 rows of the DataFrame.

    Args:
        employees (pd.DataFrame): The DataFrame containing employee data.

    Returns:
        pd.DataFrame: A DataFrame containing the first 5 rows.
    """
    return employees.head(3)


data = {'Name': ['Tom', 'Jerry', 'Mickey', 'Minnie'], 'Age': [10, 20, 30, 40]}
df = pd.DataFrame(data)
print(selectFirstRows(df))  # Output: [4, 2]