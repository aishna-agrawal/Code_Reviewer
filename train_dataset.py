import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import pickle

def train_dataset():
    data = pd.read_csv('Jm1.csv')  
    parameters=data[['v(g)','n','v','l','d','i','e','t','n1', 'n2', 'N1', 'N2']]
    X = np.asarray(parameters)
    y = np.asarray(data['result'])
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state=1)

    classifier = SVC(kernel='rbf',gamma=0.001,C=1000)
    classifier.fit(X_train,y_train)
    pickle.dump(classifier, open("SVM.sav", 'wb'))

train_dataset()

#This is only used while training dataset periodically.
