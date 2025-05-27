import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary'] * 2
    return employees


data = {'name': ['Tom', 'Jerry', 'Mickey', 'Minnie'], 'salary': [105, 101, 101, 140]}
df = pd.DataFrame(data)
print(modifySalaryColumn(df))  # Output: [4, 2]