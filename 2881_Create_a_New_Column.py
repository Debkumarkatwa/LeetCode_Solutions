import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary'] * 2
    return employees

data = {'name': ['Tom', 'Jerry', 'Mickey', 'Minnie'], 'salary': [105, 101, 101, 140]}
df = pd.DataFrame(data)
print(createBonusColumn(df))  # Output: [4, 2]