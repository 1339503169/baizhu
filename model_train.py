from utils.process_xlsx_file import process_xlsx,regularit,valid_data_scaler
import keras
import sklearn
import numpy as np
from sklearn.preprocessing import normalize,MinMaxScaler,StandardScaler
import pandas as pd

# xlsx文件地址吧
filepath='data/恒瑞.xlsx'
# 处理得到训练数据
train_x,train_y=process_xlsx(filepath,'Sheet2')
# 对数据进行归一化
sca=MinMaxScaler()
train_y=np.asarray(train_y).reshape(-1,1)
train_y=sca.fit_transform(train_y)

df=pd.DataFrame(train_x)
train_x,feature_info=regularit(df)
# 模型构建部分
from keras.models import Sequential
model = Sequential()
from keras.layers import Dense, Activation
model.add(Dense(units=128, input_dim=9))
model.add(Activation("relu"))
model.add(Dense(units=1))
model.add(Activation("softmax"))
model.summary()
model.compile(loss='mean_absolute_percentage_error', optimizer='sgd', metrics=['accuracy'])
model.fit(train_x, train_y, epochs=1000, batch_size=16,validation_split=0.2,shuffle=True)
model.save('model/train.h5')

# # 预测数据做归一化 单个数据直接调用函数，一组数据则列表推导式
#
predict=[12.61,207892,2600708,12.73,12.2,0.27,-0.4,4.34,12.66]
predict=np.asarray(predict)
y_predict=model.predict(valid_data_scaler([predict.reshape(1,9)],feature_info))
y=sca.inverse_transform(y_predict)
# predict=[[],[]]
# predict=[valid_data_scaler(i.reshape(1,8),feature_info) for i in predict]
# y_predict=model.predict(predict,batch_size=16)
# y=sca.inverse_transform([y_predict])












