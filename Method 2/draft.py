import pandas as pd
import numpy as np

a  = pd.DataFrame(np.random.randint(0,2,size=(3, 2)), columns=['Raise','Call'])
b = pd.DataFrame(np.random.randint(0,1,size=(3, 2)), columns=['Raise','Call'])
print(a)
print(b)
bmall = b.loc[~(b==0).all(axis=1)]
for index, row in a.iterrows():
    a.iloc[index, :] += 0.3 * bmall.iloc[index, :]
    b.iloc[index, :] *= 0.4
print(a)
print(b)