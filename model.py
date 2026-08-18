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