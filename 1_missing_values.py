'''
欠損値の確認
'''
import pandas as pd

data_folder = '.\\data\\'
train_file_name = 'train.tsv'

train_file_path = data_folder + train_file_name

train = pd.read_table(train_file_path, encoding='UTF8')

# 欠損値の確認
print(train.info())

'''
id          445 non-null int64
survived    445 non-null int64
pclass      445 non-null int64
sex         445 non-null object
age         360 non-null float64
sibsp       445 non-null int64
parch       445 non-null int64
fare        445 non-null float64
embarked    443 non-null object
'''
