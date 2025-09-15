import numpy as np
L={1,34,"Venya", 8.90}
print(type(L))
arr=np.array([[3,4,5,67,78,] , [45,67,8,7,9]])
print(type(arr))
print(arr.ndim)
arr=np.arange(1,21).reshape(5,4)
print(arr.shape)
print(arr.ndim)
print(arr.dtype)
print(arr.shape)

import numpy as np
#Q1
arr=np.arange(5,25).reshape(5,4)
print(arr)

#Q2
print(arr.shape)
print(arr.size)
print(arr.dtype)

#Q3
arr=np.random.randint(10,51, size=(3,4))
print(arr)
arr1= np.array([2,4,6,8,10])
arr2= np.array([1,3,5,7,9])
print(arr1+arr2)
print(arr1 - arr2)
print(arr1*arr2)
print(arr1/arr2)

#Q4
arr3 = np.arange(1,10).reshape(3,3)
print(arr3)
result = arr3 * 5
print(result)

#Q5
arr4 = np.arange(10,26).reshape(4,4)
print("Original Array\n" , arr4)
print(arr4[1])
print(arr4[:,-1])
arr4[0] = 0
print(arr4)

#Q6
arr = np.random.randint(20,41,10)
print(arr)
print("Elements >30:" , arr[arr>30])

#Q7
arr = np.arange(11,23)
print(arr)

reshaped = arr.reshape(3,4)
print(reshaped)

#Q8
A = np.array([[1,2] , [3,4]])
B = np.array([[5,6] , [7,8]])
print(np.dot(A,B))
print(A.T)

# Q9
arr=np.random.randint(10,60,size=(15))
print(arr)
print(np.mean(arr))
print(np.median(arr))
print(np.std(arr))

# Q10
arr=np.random.randint(1,10,size=(3,3))
print(arr)
print("\n")
a=np.linalg.det(arr)
print(a)
b=np.linalg.inv(arr)
print(b)
c=np.linalg.eig(arr)
print(c)

# Q11
import numpy as np

pos= np.array([[0,0], [2,3], [4,7], [7,10], [10,15]])
#now for euclidon dist.
d=np.linalg.norm(pos[-1]-pos[0])
print(d)

steps=np.diff(pos,axis=0)
distance=np.linalg.norm(steps,axis=1)
total=np.sum(distance)
print(d)
print(total)


