from sklearn import tree
import csv

file = open('train.csv',"r")
titanic_csv = csv.reader(file)
titanic_train = [] 
titanic_train_labels=[]
for value in titanic_csv:
	#print(" P_class={} Sex-{} Age-{} No_of_sib-{} No_of_p-{} ".format(value[2],value[4],value[5],value[6],value[7]))
	temp=[value[2],value[4],value[5],value[6],value[7]]
	titanic_train.append([temp])
	titanic_train_labels.append(value[1])

for value1,value2 in zip(titanic_train,titanic_train_labels):
	if(value2 == 1):
		print("The passenger {} has survived".format(value1))
	else:
		print("The passenger {} hasn't survived".format(value1))
#creating the classifier 

clf = tree.DecisionTreeClassifier()
clf = clf.fit(titanic_train,titanic_train_labels)

print("Enter the passengerClass,Sex,AGE,No_of_sib,No_of_p seperated by , below")
u_input = [x for x in input("Input: ").split(",")]

print(clf.predict(u_input))