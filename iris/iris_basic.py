from sklearn import tree
features = [[ 5.1,3.5,1.4,0.2],[4.9,3.0,1.4,0.2],[5.5,2.4,3.7,1.0],[6.0,2.7,5.1,1.6]]
labels = ["Iris-setosa","Iris-setosa","Iris-versicolor","Iris-versicolor"]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print(clf.predict([[5.7,4.4,1.5,0.4]]))