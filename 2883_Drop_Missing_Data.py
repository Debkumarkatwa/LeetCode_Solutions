import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(axis=0, subset=['name'])
    # return students.drop(students[students['name'] == ''].index)


data = {'name': ['Tom', None, 'Mickey', 'Minnie'], 'salary': [None, 101, 101, 140]}
df = pd.DataFrame(data)
print(dropMissingData(df))  # Output: [4, 2]