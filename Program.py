class Row:
    data = []
    target = 0;
    def __init__(self,data,target):
        self.data = data;
        self.target = target;
    def __str__(self):
        listStr = "";
        #for i in self.data:
        #    listStr += str(i)+" ";
        #retVal = "";
        #retVal += "Data: " + listStr;
        retVal += "\nTarget: " + str(self.target);
        return retVal;
import csv
class Model:
    rows = [];
    def __init__(self):
        self.rows = [];
    def toListRow(self):
        rowsList = [];
        for row in self.rows:
            rowsList.append(row.data);
        return rowsList;
    def toListTarget(self):
        rowsList = [];
        for row in self.rows:
            rowsList.append(row.target);
        return rowsList;
    def addRow(self,valueList,target):
        row = Row(valueList,target);
        self.rows.append(row);
count = -1
trainingModel = Model();
testModel = Model();
import random as r
with open('train.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        count += 1;        
        if(count == 0):
            continue;
        addThis = []
        testSelect = r.randint(1,200);
        for rec in row[0:1582]:
            addThis.append(float(rec));
        if(testSelect == 3):
            #print("Dodajem u test");
            testModel.addRow(addThis,int(row[1582]));
        else:
            #print("Dodajem u trening set");
            trainingModel.addRow(addThis,int(row[1582]));
        if(count > 666):
            break;
print(len(trainingModel.toListTarget()))
print(len(testModel.toListTarget()))
from sklearn.naive_bayes import GaussianNB

from sklearn import svm
clf = svm.SVC()
vracara = clf.fit(trainingModel.toListRow(), trainingModel.toListTarget())
y_pred = vracara.predict(testModel.toListRow())
import numpy as np
from sklearn.metrics import accuracy_score

y_true = testModel.toListTarget();
#print(testModel.toListTarget())
print(accuracy_score(y_true, y_pred))



