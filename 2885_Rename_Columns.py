import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students.rename(columns={'id': 'student_id', 'first': 'first_name', 'last': 'last_name', 'age': 'age_in_years'}, inplace=True)
    return students

data = {'id': ['Tom', 'Jerry', 'Mickey', 'Minnie'], 'first': [105, 101, 101, 140], 'last': [105, 101, 101, 140], 'age': [105, 101, 101, 140]}
df = pd.DataFrame(data)
print(renameColumns(df))  # Output: [4, 2]