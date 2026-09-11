#question 5

from sklearn.naive_bayes import GaussianNB
x=[[25],[30],[35],[40],[50],[60],[65]]
y=["fail","fail","fail","pass","pass","pass","pass"]
model=GaussianNB()
marks=[[42]]
model.fit(x,y)
prediction=model.predict(marks)
print(prediction)



#question 4

from sklearn.svm import SVC
x=[[15000],[18000],[20000],[25000],[30000],[40000],[50000]]
y=["not buy","not buy","not buy","buy","buy","buy","buy"]
model=SVC(kernel="linear")
model.fit(x,y)
salary=[[41000]]
prediction=model.predict(salary)
print(prediction)


#question 3

from sklearn.neighbors import KNeighborsClassifier
x=[[-2],[-1],[2],[18],[20],[22],[25],[30],[32],[35],[38]]
y=["cold","cold","cold","normal","normal","normal","normal","hot","hot","hot","hot"]
model=KNeighborsClassifier(n_neighbors=3)
model.fit(x,y)
temprature=[[-2]]
prediction=model.predict(temprature)
print(prediction)



#question 2

from sklearn.tree import DecisionTreeClassifier
x=[[45],[50],[60],[70],[75],[80],[85],[90]]
y=["not eligible","not eligible","not eligible","eligible","eligible","eligible","eligible","eligible"]
model=DecisionTreeClassifier()
model.fit(x,y)
attendence=[[88]]
prediction=model.predict(attendence)
print(prediction)



#question 1:

from sklearn.tree import DecisionTreeClassifier
x=[[1],[2],[3],[4],[5],[6],[7]]
y=["fail","fail","fail","pass","pass","pass","pass"]
model=DecisionTreeClassifier()
model.fit(x,y)
hours=[[2.5]]
prediction=model.predict(hours)
print(prediction)





#mlp classifier

from sklearn.neural_network import MLPClassifier
x=[[1],[2],[4],[5]]
y=["fail","fail","pass","pass"]
model=MLPClassifier(hidden_layer_sizes=(2,),max_iter=5000,random_state=42)
model.fit(x,y)
hours=[[5]]
prediction=model.predict(hours)
print(prediction)

#svm

from sklearn.svm import SVC
x=[[1],[2],[3],[4]]
y=["fail","fail","pass","pass"]
model=SVC(kernel="linear")
model.fit(x,y)
hours=[[0]]
prediction=model.predict(hours)
print(prediction)

#knn

from sklearn.neighbors import KNeighborsClassifier
x=[[1],[2],[3],[4]]
y=["fail","fail","pass","pass"]
model=KNeighborsClassifier(n_neighbors=3)
model.fit(x,y)
hours=[[9]]
prediction=model.predict(hours)
print(prediction)

#rule based classification

hours=int(input("enter study hours:"))
if hours>=4:
    print("pass")
else:
    print("fail")    