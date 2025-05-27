import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students['grade'].astype(int)
    return students


data = {'name': ['Tom', 'Jerry', 'Mickey', 'Minnie'], 'grade': [105.08, 101.80, 101.00, 140]}
df = pd.DataFrame(data)
print(changeDatatype(df))  # Output: [4, 2]
