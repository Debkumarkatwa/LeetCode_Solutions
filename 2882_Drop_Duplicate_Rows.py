import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    """
    This function takes a DataFrame of customers and returns a DataFrame with duplicate emails dropped.
    The first occurrence of each email is kept, and subsequent duplicates are removed.
    """
    return customers.drop_duplicates(subset='email', keep='first')


data = {'name': ['Tom', 'Jerry', 'Jerry', 'Minnie'], 'salary': [105, 101, 101, 140]}
df = pd.DataFrame(data)
print(dropDuplicateEmails(df))  # Output: [4, 2]