import numpy as np
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, cross_val_predict
from sklearn.metrics import accuracy_score, classification_report

iris = load_iris()
x, y = iris.data, iris.target 

class_names = iris.target_names

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=51)

clf = DecisionTreeClassifier(random_state=51)

y_pred = cross_val_predict(clf, x, y, cv=5)

accuracy = accuracy_score(y, y_pred)
print("Accuracy: ", accuracy)
print('\n')

print("Classification Report: ")
print(classification_report(y, y_pred, target_names=class_names))