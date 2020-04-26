# -*- coding: utf-8 -*-
import numpy as np
from MQ.Bert.bert.extract_feature import BertVector
from MQ.Bert.load_data import train_df, test_df
from keras.utils import to_categorical
from keras.models import Model
from keras.optimizers import Adam
from keras.layers import Input, BatchNormalization, Dense
import matplotlib.pyplot as plt
# 读取文件并进行转换
# 统一长度取470
bert_model = BertVector(pooling_strategy="REDUCE_MEAN", max_seq_len=470)
print('begin encoding')
f1 = lambda text: bert_model.encode([text])["encodes"][0]
train_df['x'] = train_df['text'].apply(f1)
test_df['x'] = test_df['text'].apply(f1)
print('end encoding')

x_train = np.array([vec for vec in train_df['x']])
x_test = np.array([vec for vec in test_df['x']])
y_train = np.array([vec for vec in train_df['label']])
y_test = np.array([vec for vec in test_df['label']])
print('x_train: ', x_train.shape)

# Convert class vectors to binary class matrices.
num_classes = 8  # 标签个数
y_train = to_categorical(y_train, num_classes)
y_test = to_categorical(y_test, num_classes)

# 创建模型
x_in = Input(shape=(768,))
x_out = Dense(32, activation="relu")(x_in)
x_out = BatchNormalization()(x_out)
x_out = Dense(num_classes, activation="softmax")(x_out)
model = Model(inputs=x_in, outputs=x_out)
print(model.summary())

model.compile(loss='categorical_crossentropy',
              optimizer=Adam(),
              metrics=['accuracy'])

# 模型训练以及评估
history = model.fit(x_train, y_train, validation_data=(x_test, y_test), batch_size=8, epochs=20)
# model.fit(x_train, y_train, batch_size=8, epochs=20)
model.save('./model/model2.h5')
print(model.evaluate(x_test, y_test))

# 绘制loss和acc图像
plt.subplot(2, 1, 1)
epochs = len(history.history['loss'])
plt.plot(range(epochs), history.history['loss'], label='loss')
plt.plot(range(epochs), history.history['val_loss'], label='val_loss')
plt.legend()

plt.subplot(2, 1, 2)
epochs = len(history.history['acc'])
plt.plot(range(epochs), history.history['acc'], label='acc')
plt.plot(range(epochs), history.history['val_acc'], label='val_acc')
plt.legend()
plt.show()

plt.savefig("./data/loss_acc.png")

