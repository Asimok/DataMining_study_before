# 查看其中一个地区的训练数据
import matplotlib.pyplot as plt
import pandas as pd
from keras.layers import Dense, LSTM, Flatten
from keras.models import Sequential
from pandas import concat
from sklearn.preprocessing import MinMaxScaler

columns = ['年', '月', '日', 'AQI', '质量等级', 'PM2.5', 'PM10', 'SO2', 'CO', 'NO2', 'O3_8h']
data = pd.read_excel('./data/new.xlsx', names=columns)
data.head()

# 数据预处理
# 数据预处理：将序列数据转化为监督问题数据
from pandas import DataFrame


def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
    n_vars = 1 if type(data) is list else data.shape[1]
    df = DataFrame(data)
    cols, names = [], []
    # i: n_in, n_in-1, ..., 1
    # 代表t-n_in, ... ,t-1
    for i in range(n_in, 0, -1):
        cols.append(df.shift(i))
        names += [('var%d(t-%d)' % (j + 1, i)) for j in range(n_vars)]
    for i in range(0, n_out):
        cols.append(df.shift(-i))
        if i == 0:
            names += [('var%d(t)' % (j + 1)) for j in range(n_vars)]
        else:
            names += [('var%d(t+%d)' % (j + 1, i)) for j in range(n_vars)]
    agg = concat(cols, axis=1)
    agg.columns = names
    if dropnan:
        agg.dropna(inplace=True)
    return agg


# 将数据归一化到0-1之间,无量纲化
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(data[['AQI', 'PM2.5', 'PM10', 'SO2', 'CO', 'NO2', 'O3_8h']].values)

# 将时序数据转换为监督问题数据
reframed = series_to_supervised(scaled_data, 1, 1)

# 删除无用的label数据
reframed.drop(reframed.columns[[6, 7, 8, 9]], axis=1, inplace=True)
print(reframed.info())
reframed.head()

# 数据互粉
# 数据集划分,选取前400天的数据作为训练集,中间150天作为验证集,其余的作为测试集
train_days = 1800
valid_days = 200
values = reframed.values
train = values[:train_days, :]
valid = values[train_days:train_days + valid_days, :]
test = values[train_days + valid_days:, :]
train_X, train_y = train[:, :-1], train[:, -1]
valid_X, valid_y = valid[:, :-1], valid[:, -1]
test_X, test_y = test[:, :-1], test[:, -1]

# 将数据集重构为符合LSTM要求的数据格式,即 [样本，时间步，特征]
train_X = train_X.reshape((train_X.shape[0], 1, train_X.shape[1]))
valid_X = valid_X.reshape((valid_X.shape[0], 1, valid_X.shape[1]))
test_X = test_X.reshape((test_X.shape[0], 1, test_X.shape[1]))
print(train_X.shape, train_y.shape, valid_X.shape, valid_y.shape, test_X.shape, test_y.shape)

# 使用Keras的Sequential搭建模型
model = Sequential()
model.add(LSTM(50, activation='relu', input_shape=(train_X.shape[1], train_X.shape[2]), return_sequences=True))
model.add(Flatten())
model.add(Dense(1, activation='linear'))
model.compile(loss='mean_squared_error', optimizer='adam')
model.summary()

# fit network
hist = model.fit(train_X, train_y, epochs=180, batch_size=10, validation_data=(valid_X, valid_y), verbose=1,
                 shuffle=False)

# plot history
plt.plot(hist.history['loss'], label='train')
plt.plot(hist.history['val_loss'], label='valid')
plt.legend()
plt.show()

# 查看预测结果
plt.figure(figsize=(24, 8))
train_predict = model.predict(train_X)
valid_predict = model.predict(valid_X)
test_predict = model.predict(test_X)
plt.plot(values[:, -1], c='b', label="Train set (actual)")
plt.plot([x for x in train_predict], c='g', label="Train set (predict)")
plt.plot([None for _ in train_predict] + [x for x in valid_predict], c='y', label="Valid set (predict)")
plt.plot([None for _ in train_predict] + [None for _ in valid_predict] + [x for x in test_predict], c='r',
         label="Test set (predict)")
plt.legend(fontsize=16)
plt.show()
plt.savefig('./data/ans.png')
