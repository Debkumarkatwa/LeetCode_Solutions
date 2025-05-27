import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return report.melt(id_vars=['product'], 
                      var_name='quarter', 
                      value_name='sales')

# Example usage
data = {
    'product': ['A', 'B', 'C', 'D'],
    'Q1': [100, 200, 300, 400],
    'Q2': [110, 210, 310, 410],
    'Q3': [120, 220, 320, 420],
    'Q4': [130, 230, 330, 430]
}
df = pd.DataFrame(data)
result = meltTable(df)
print(result)