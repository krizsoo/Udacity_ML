#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score


data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### split data
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, random_state=42)

### set up deicision tree
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(random_state=0)
clf.fit(features_train,labels_train)
print clf.score(features_test,labels_test)
prediction = clf.predict(features_test)

counter = 0
for i in prediction:
    counter += i

print counter

true_positives = 0
for i in range(len(prediction)):
    if prediction[i] == labels_test[i] and prediction[i] == 1:
        true_positives += 1

print true_positives

print precision_score(prediction, labels_test)
print recall_score(prediction, labels_test)
