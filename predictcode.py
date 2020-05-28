import numpy as np
import pandas as pd
import pickle
from sklearn.svm import SVC

def arr_input(arr):
    arr=np.asarray(arr)
    arr=arr.reshape(1,-1)
    classifier = pickle.load(open("SVM.sav", 'rb'))
    y_pred = classifier.predict(arr)
    arr = list(arr)
    arr.append(y_pred)
    # print(y_pred)
    return y_pred
    