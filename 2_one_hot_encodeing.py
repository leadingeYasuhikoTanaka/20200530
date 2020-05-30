'''
ダミー変数化
'''
import pandas as pd

data_folder = 'C:\\Dev\\zz_data\\04_KnowHow\\11_SIGNATE\\02_titanic\\data\\'
train_file_name = 'train.tsv'
train_dummy_file_name = 'train_dummies.csv'
predict_file_name='predict.tsv'
predict_dummy_file_name = 'predict_dummies.csv'

train_file_path = data_folder + train_file_name
train_dummy_file_path = data_folder + train_dummy_file_name
predict_file_path = data_folder + predict_file_name
predict_dummy_file_path = data_folder + predict_dummy_file_name

train = pd.read_table(train_file_path, encoding='UTF8')
predict = pd.read_table(predict_file_path, encoding='UTF8')

# ダミー変数化
train_dummy = pd.get_dummies(train)
print(train_dummy)
predict_dummy=pd.get_dummies(predict)
print(predict_dummy)

# # # 結果ファイル作成
train_dummy.to_csv(train_dummy_file_path, sep='\t',index=None)
predict_dummy.to_csv(predict_dummy_file_path, sep='\t',index=None)
