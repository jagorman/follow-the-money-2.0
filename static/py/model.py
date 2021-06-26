import pandas as pd
from keras.utils import to_categorical
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

cont_df = pd.read_csv('../../resources/processed_data.csv')
cont_data = cont_df.values
X = cont_data[:, 3:]
y = cont_data[:, 2]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=1)
X_scaler = MinMaxScaler().fit(X_train)
X_train_scaled = X_scaler.transform(X_train)
X_test_scaled = X_scaler.transform(X_test)

label_encoder = LabelEncoder()
label_encoder.fit(y_train)
encoded_y_train = label_encoder.transform(y_train)
encoded_y_test = label_encoder.transform(y_test)
one_hot_y_train = to_categorical(encoded_y_train)
one_hot_y_test = to_categorical(encoded_y_test)

model = Sequential()
model.add(Dense(units=100, activation='relu', input_dim=118))
model.add(Dense(units=100, activation='relu'))
model.add(Dense(units=2, activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy',
              metrics=['accuracy'])
model.fit(X_train_scaled, one_hot_y_train, epochs=60, shuffle=True, verbose=0)

model_loss, model_accuracy = model.evaluate(
    X_test_scaled, one_hot_y_test, verbose=2)
print(
    f"Normal Neural Network - Loss: {model_loss}, Accuracy: {model_accuracy}")
model.save('contributor_model.h5')
