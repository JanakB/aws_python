import numpy as np
import pandas as pd


class MinMaxNorm:
    def scale(self, df):
        for c in df.columns:
            min = df[c].min()
            max = df[c].max()
            df[c] = (df[c] - min) / (max - min)
        return df


df = pd.DataFrame(
    [[65000, 32], [56000, 36], [76000, 44], [45000, 34]], columns=["Salary", "Age"]
)
print("Original Data")
print(df)

s = MinMaxNorm()
df_scaled = s.scale(df)

print("\nScaled Data")
print(df_scaled)

