import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products['price'].fillna(0, inplace=True)
    products['quantity'].fillna(0, inplace=True)
    return products

data = {'product': ['apple', 'banana', 'orange', 'grape'],
        'price': [1.2, None, 0.8, None],
        'quantity': [10, 20, None, 15]}
df = pd.DataFrame(data)
print(fillMissingValues(df))