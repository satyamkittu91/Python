import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris_dataset = load_iris()

#print("keys of the iris_dataset: \n{}".format(iris_dataset.keys()))
#print("\n" + iris_dataset['DESCR'] + "\n")
#print("Target names: {}".format(iris_dataset['target_names']))

#print("Types of data: {}".format(type(iris_dataset['data'])))
#print("shape of data: {}".format(iris_dataset['data'].shape))

X_train, x_test, y_train, y_test = train_test_split(
    iris_dataset['data'], iris_dataset['target'], random_state=0
)

#print("X_train shape: {}".format(X_train.shape))
#print("y_train shape: {}".format(y_train.shape))
#print("x_test shape: {}".format(x_test.shape))
#print("y_test shape: {}".format(y_test.shape))

'''
iris_dataset = pd.DataFrame(X_train, columns=iris_dataset['feature_names'])

grr = pd.plotting.scatter_matrix(iris_dataset, c=y_train, figsize=(15, 15), marker='o',
                                 hist_kwds={'bins': 20}, s=60, alpha=.8, cmap='viridis')
plt.show()
'''
knn = KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski', metric_params=None, n_jobs=1, n_neighbors=1, p=2, weights='uniform')

X_new = np.array([[5, 2.9, 1, 0.2]])
print("X_new shape: {}".format(X_new.shape))

y_pred = knn.predict(x_test)
print("Test set Predictions:\n {}".format(y_pred))