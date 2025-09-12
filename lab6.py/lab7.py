import numpy as np
list1=[[4, 3, 7],
        [4, 5, 6],
        [7, 8, 9]]

list2=[[9, 8 ,7],
         [6, 5, 4],
         [3, 2, 1]]

mat1=np.array(list1)
mat2=np.array(list2)
result=np.dot(list1,list2)
print(result)