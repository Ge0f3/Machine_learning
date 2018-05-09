#libraries
from sklearn import tree
import csv

file = open('iris.csv','r')
iris_csv = csv.reader(file)
next(iris_csv)

iris_train = []
iris_label = []
for species in iris_csv:
	temp = [species[1],species[2],species[3],species[4]]
	iris_train.append(temp)
	iris_label.append(species[5])

# print(iris_train)
clf= tree.DecisionTreeClassifier()
clf= clf.fit(iris_train,iris_label)

print(clf.predict([[5.7,4.4,1.5,0.4]]))

print("Enter the SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm seperated by ,")
u_input = [float(x) for x in input("Input: ").split(",")]
predict =[] 
predict.append(u_input)

print(clf.predict(predict))

