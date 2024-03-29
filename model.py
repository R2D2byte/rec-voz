import numpy as np
import pandas as pd
import joblib
import math
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def train_new_data():
    dataset = pd.read_csv('dataset.csv')
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 1)

    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    n_samples, n_features = X_train.shape
    n_components = min(n_samples, n_features)

    pca = PCA(n_components=n_components)
    df_pca = pca.fit_transform(X_train)
    df_pca = pd.DataFrame(data=df_pca, columns=[f'PC{i+1}' for i in range(n_components)])
    joblib.dump(pca, 'modelo_pca.pkl')

    X_train = df_pca.values 
    k = int(math.sqrt(len(X_train)))

    classifier = KNeighborsClassifier(n_neighbors = k, metric = 'minkowski', p = 2)
    classifier.fit(X_train, y_train)
    modelo_pca = joblib.load('modelo_pca.pkl')
    X_test = pca.transform(X_test)
    y_pred = classifier.predict(X_test)
    print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

    from sklearn.metrics import confusion_matrix, accuracy_score
    cm = confusion_matrix(y_test, y_pred)
    print(cm)
    print(accuracy_score(y_test, y_pred))

    joblib.dump(classifier, 'modelo_knn.joblib')
    joblib.dump(sc, 'scaler.joblib')

train_new_data()