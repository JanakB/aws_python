import numpy as np
import pandas as pd

class StandardNorm:
    def scale(self, df):
        for i in df.columns:
            mean = df[i].mean()
            sd = df[i].std()
            df[i] = (df[i] - mean) / sd
        return df

df = pd.DataFrame(
    [[65000, 32], [56000, 36], [76000, 44], [45000, 34]], columns=["Salary", "Age"]
)
print("Original Data")
print(df)

s = StandardNorm()
df_scaled = s.scale(df)

print("\nScaled Data")
print(df_scaled)