import pandas as pd

def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
    b,c = [],[]
    for i in student_data:
        b.append(i[0])
        c.append(i[1])
    return pd.DataFrame({'student_id': b, 'age': c})



student_data = [[1, 20], [2, 21], [3, 22]] 
df = createDataframe(student_data)
print(df)