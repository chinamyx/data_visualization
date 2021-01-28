import pandas as pd
import numpy as np

y = pd.DataFrame(0.0001*np.random.randint(0,10000,size=(100,100)))
y.to_csv(r"Coursera\ppd1\write1.csv")
y = pd.read_csv(r"Coursera\ppd1\write1.csv", index_col = 0) #index_col to remove unnamed columns #read converts columns to string
y = y.sort_values(['0','1','2'])

y.to_csv(r"Coursera\ppd1\write1.csv")



columns_titles = y.columns.values

df_reorder=df.reindex(columns=columns_titles)
df_reorder.to_csv('/Users/parent/Desktop/col_reorder1.csv', index=False)
print(df_reorder)

# y = y[['2','5','3']]  to rearrange columns
# print(y.head())
# print(f"\n the columns are : {y.columns.values}")
# print(f"\n the index are : {y.index.values}")

#References
#https://kanoki.org/2019/03/23/pandas-rename-and-reorder-columns/ (Rename Columns)
#https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html (matplot lib api)
#https://www.youtube.com/watch?v=UO98lJQ3QGI (tutorial to follow)




