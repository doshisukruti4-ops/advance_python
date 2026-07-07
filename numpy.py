import numpy as np
#version
print(np.__version__)
#2 dimention array
ar=np.array([[1,2,3,4],[10,20,30,40]])
print(ar)
print(ar.shape)
print(ar.size)
print(ar.dtype)
print(ar.ndim)
#concatination
list1=[1,2,3]
list2=[4,5,6]
arr2=np.array([list1+
               list2])
print(arr2)

#id
id_arr=np.eye(3)
print(id_arr)

#randome number pic
r=np.random.randint(1,20)
print(r)

#string array
arr=np.array(["shyam","ram","jay","kavita"])
print(arr)

#start:stop:step
a=np.array([1,3,5,7,9])
print(a[0:5:2])

#rows and columns
std=np.array(
    [[1,2,3],[10,20,30]])

print(std)
print(std[1][2])
print(std[:,0])

#convert rows into columns
rto=np.array([10,20,30,40,50])
reshaped=rto.reshape((5,1))
print(reshaped)

#array stacking and splitting
a=np.array([11,22,33])
b=np.array([4,5,6])
print(np.hstack((a,b)))
print(np.vstack((a,b)))