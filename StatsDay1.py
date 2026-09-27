print("day 1 of learning statistics")

import pandas as pd

df=pd.read_csv("C:/Users/User/Downloads/archive (1)/retail_sales_dataset.csv")
print(df)

df.head(5)

df.describe()