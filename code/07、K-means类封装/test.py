import pandas as pd

iris = pd.read_csv('./iris_data/iris.csv')
iris = iris.groupby('Species').apply(lambda x: x)

print(iris)
