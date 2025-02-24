import numpy as np
import pandas as pd

data = pd.read_csv('./iris_data/iris.csv')
data = data.iloc[:, :-1]
data = data.to_numpy()
print(data)

a = np.argmin(data, axis=0)
print(a)
