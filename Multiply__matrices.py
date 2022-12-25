# Multiply Array

array=[[1,2,3],[4,5,6],[7,8,9]]
array1=[[1,3,5],[7,5,9],[7,3,9]]
arrayres=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            arrayres[i][j] += array[i][j]*array1[i][j]

for r in arrayres:
   print(r)