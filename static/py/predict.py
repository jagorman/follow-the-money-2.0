import pandas as pd
import numpy as np
from keras.utils import to_categorical
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential, load_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

model = load_model('contributor_model.h5')


def predict(d):
    party = ''
    data_array = np.array([[int(s) for s in d.split(',')]])
    party_pred = model.predict(data_array)
    if party_pred[0][0] >= .5:
        party = 'Republican'
    else:
        party = 'Democrat'
    return str(party)
