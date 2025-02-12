import pandas as pd

# 简单的数据读取和展示
file = "./titanic_data/train.csv"
data = pd.read_csv(file)
# print(data)

# 简单数据清洗示例
data = data[data['Survived'] != 0]

print(data)
