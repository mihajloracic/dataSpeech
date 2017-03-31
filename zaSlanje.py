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
##READING TRAIGING DATA
with open('train.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        count += 1;        
        if(count == 0):
            continue;
        addThis = []
        for rec in row[0:1582]:
            addThis.append(float(rec));
        trainingModel.addRow(addThis,int(row[1582]));
##READING TEST DATA
count = -1;
with open('test.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        count += 1;        
        if(count == 0):
            continue;
        addThis = []
        for rec in row[0:1582]:
            addThis.append(float(rec));
        testModel.addRow(addThis,int(0));

print("Komada u trening modelu: ",len(trainingModel.toListTarget()))
print("Komada u test modelu: ",len(testModel.toListTarget()))
print("FINISHED READING TEST AND TRAING FILES");
from sklearn.svm import LinearSVC
#SET up suport vector machine
clf = LinearSVC(penalty='l2', loss='squared_hinge',
                dual=False, tol=0.00000001,
                C=1.0, multi_class='ovr',
                fit_intercept=True, intercept_scaling=1,
                class_weight=None, verbose=0,
                random_state=None, max_iter=1000)
print("TRAINING STARTED");
#TRAINING
vracara = clf.fit(trainingModel.toListRow(), trainingModel.toListTarget())
print("TRAINING FINSHED SUCESFULLY");
#PREDICTION
print("PREDICTION STARTED");
y_pred = vracara.predict(testModel.toListRow())
print("PREDICTION FINISHED SUCESFULLY");
out = "";
for val in y_pred:
    out += str(val) +  "\n";

text_file = open("klasifikacija.txt", "w")

text_file.write(out)

text_file.close()
