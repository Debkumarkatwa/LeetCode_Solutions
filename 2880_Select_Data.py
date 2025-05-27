import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    a = students[students['student_id'] == 101]
    
    return pd.DataFrame({'name': a['name'].tolist(), 'age': a['age'].tolist()})


data = {'name': ['Tom', 'Jerry', 'Mickey', 'Minnie'], 'student_id': [105, 101, 101, 140], 'age': [105, 101, 101, 140]}
df = pd.DataFrame(data)
print(selectData(df))  # Output: [4, 2]