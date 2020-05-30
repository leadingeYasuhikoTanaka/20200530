# 1. 性別+客室
# 2. 性別+客室+乗船港CとQ
# 3. 性別+客室+乗船港CとQ+乗船していた兄弟・配偶者の数が3人以上かどうか
# 4. 性別+客室+乗船港CとQ+乗船していた兄弟・配偶者の数が3人以上かどうか+年齢
# 5. 性別+客室+乗船港CとQ+乗船していた兄弟・配偶者の数が3人以上かどうか+年齢+乗船していた両親・子供の数
#
# 性別 A
# 客室 A
# 船賃 A ⇒ 客室と多重共線性強い
# 乗船した港 A
# 　ただし embarked_S⇒CとQと多重共線性強
# 乗船していた兄弟・配偶者の数 ⇒3人以上かどうか　A
# 年齢 B
# 乗船していた両親・子供の数 C
# パターン

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

data_folder = '.\\data\\'
train_file_name = 'train_dummies_final.tsv'
predict_file_name = 'predict_dummies_final.tsv'
submit_file_name = 'submit4.tsv'

train_file_path = data_folder + train_file_name
predict_file_name=data_folder + predict_file_name
submit_file_path = data_folder + submit_file_name

# 訓練データのロード
train = pd.read_table(train_file_path, encoding='UTF8')
# 予測データのロード
predict =pd.read_table(predict_file_name, encoding='UTF8')
# print(predict)
# 前処理：欠損値を含む行を削除
train = train.dropna()
# print(train)

# 目的変数
train_y=train['survived']

#説明変数
trainX = train[
  [
    'sex_female'
    ,'pclass'
    ,'embarked_C'
    ,'embarked_Q'
    ,'sibsp_2'
    ,'age'
    # ,'parch's
  ]
]
# print(trainX)

# 訓練データと検証データの分割
X_train, X_test, y_train, y_test = train_test_split(trainX, train_y, test_size = 0.25,random_state=22)

# ロジスティク回帰のインスタンス化
logi_model=LogisticRegression()
logi_model.fit(X_train,y_train)

#過学習の確認
#決定係数の確認：検証データ
print(logi_model.score(X_test,y_test))
#決定係数の確認：訓練データ
print(logi_model.score(X_train,y_train))
'''
0.7111111111111111
0.8296296296296296
'''

#予測データ
predictX = predict[
  [
    'sex_female'
    ,'pclass'
    ,'embarked_C'
    ,'embarked_Q'
    ,'sibsp_2'
    ,'age'
    # ,'parch's
  ]
]
#欠損値処理
predictX = predictX.fillna(predictX["age"].mean())
# print(predictX)

# 予測値を算出してpredに代入
pred = logi_model.predict_proba(predictX)

target = pd.DataFrame(index=[], columns=[])
#tagertに、IDを書き込む
# print(predict['id'])
target[0] = predict['id']
#tagertに、生存確率を書き込む
target[1] = pred[:,1]
#TSVへ出力
target.to_csv(submit_file_path,sep='\t',header=None, index = None)
