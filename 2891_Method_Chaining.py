import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    a = animals[animals['weight'] > 100]
    a = a.sort_values(by='weight', ascending=False)

    return a['name'].tolist()

# Example usage
data = {'name': ['Elephant', 'Mouse', 'Giraffe', 'Lion'], 'weight': [120, 0.5, 800, 190]}
df = pd.DataFrame(data)
print(findHeavyAnimals(df))  # Output: ['Elephant', 'Giraffe', 'Lion']
