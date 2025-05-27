import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> list[int]:
    return list(players.shape)

data = {'Name': ['Tom', 'Jerry', 'Mickey', 'Minnie'], 'Age': [10, 20, 30, 40]}
df = pd.DataFrame(data)
print(getDataframeSize(df))  # Output: [4, 2]