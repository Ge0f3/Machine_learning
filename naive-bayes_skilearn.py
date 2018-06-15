from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
import csv
import numpy as np
import pandas as pd


def loadCsv(filename):
	lines = csv.reader(open(filename, "r+"))
	dataset = list(lines)
	for i in range(len(dataset)):
		dataset[i] = [float(x) for x in dataset[i]]
	return dataset
def splitdataset(dataset,split_ratio):
	#test_ratio= 1-split_ratio
	train_ratio=int(split_ratio*len(dataset))
	training_data = dataset[:train_ratio]
	test_data=dataset[train_ratio:]
	print("The length of training set is {}\nThe length of testing data is {}\nThe total is {}".format(len(training_data),len(test_data),(len(training_data)+len(test_data))))
	return training_data,test_data
def get_filename():
	filename=str(input("Enter the filename or press enter: "))
	return filename

def iris_naive_bayes():
	iris = datasets.load_iris()
	gnb = GaussianNB()
	y_pred = gnb.fit(iris.data, iris.target).predict(iris.data)
	print("Number of mislabeled points out of a total {} points : {}".format(iris.data.shape[0],(iris.target != y_pred).sum()))
	print("Type is {} \nThe length is {}\nTarget Length is {}".format(type(iris.data),len(iris.data),len(iris.target)))

def main():
	dataset = pd.read_csv(filename)
	print(type(dataset))



