'''
説明変数同士のクロス集計結果
'''
import pandas as pd

data_folder = 'C:\\Dev\\zz_data\\04_KnowHow\\11_SIGNATE\\02_titanic\\data\\'
train_file_name = 'train.tsv'
train_file_path = data_folder + train_file_name

train = pd.read_table(train_file_path, encoding='UTF8')
# print(train)

# クロス集計
# 客室
print(pd.crosstab(train['pclass'], train['survived']))
"""
  survived    0(死亡)   1（生存）
  pclass
  1          34  74
  2          54  43
  3         178  62
"""

# 性別
print(pd.crosstab(train['sex'], train['survived']))
"""
  survived    0    1
  sex
  female     35  121
  male      231   58
"""

# 年齢
print(pd.crosstab(train['age'], train['survived']))
"""
  survived  0  1
  age
  0.67      0  1
  0.75      0  1
  0.83      0  1
  0.92      0  1
  1.00      1  2
  ...      .. ..
  64.00     1  0
  65.00     1  0
  66.00     1  0
  70.00     1  0
  80.00     0  1
"""

# 乗船していた兄弟・配偶者の数
print(pd.crosstab(train['sibsp'], train['survived']))
"""
  survived    0    1
  sibsp
  0         194  105
  1          47   64
  2           6    8
  3           4    2
  4           7    0
  5           2    0
  8           6    0
"""

# 乗船していた両親・子供の数
print(pd.crosstab(train['parch'], train['survived']))
"""
survived    0    1
parch
0         212  118
1          20   36
2          28   21
3           2    3
4           2    0
5           2    1
"""

# 船賃
print(pd.crosstab(train['fare'], train['survived']))
"""
  survived  0  1
  fare
  0.0000    4  0
  5.0000    1  0
  6.2375    1  0
  6.4958    1  0
  6.7500    1  0
  ...      .. ..
  211.3375  0  3
  211.5000  1  0
  227.5250  0  1
  263.0000  1  2
  512.3292  0  2
"""

# 乗船した港
print(pd.crosstab(train['embarked'], train['survived']))
"""
  survived    0    1
  embarked
  C          32   47
  Q          23   16
  S         211  114
 """
