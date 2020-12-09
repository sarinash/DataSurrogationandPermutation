import numpy as np
import pandas
from matplotlib import pyplot as pt




df = pandas.read_excel("C:/Users/sarina/Desktop/data/111.xlsx")
array = df['Idea']

array = array.values.tolist()
print(len(array))
print(array)
Zeros = np.zeros((1000, 2700))
print(len(array))

B = []
controlNum = 1
list = []
count = 0
for current in array:
    if current != controlNum:
        count += 1
    else:
        list.append(count)
        count = 0
# print(list)
for i in range(1000):
    xr = np.random.permutation(list)
    B.append(xr)

# print(B)
# A[3]=0
Index = []
# print(len(list))
for j in range(len(B)):
    new_Index = B[j]
    #print(len(new_Index))
    #print(new_Index)

    for i in range(len(new_Index)):

        if i == 0:
            In = new_Index[i]
            Index.append(In)
        else:
            In = new_Index[i] + 1 + Index[i - 1]
            Index.append(In)
    #print(Index)

    for k in range(len(Index)):
        #print(k, Index[k])

        Zeros[j][Index[k]] = 1

    #print("##############")
    Index = []
# print(Zeros)
toDataFrame = pandas.DataFrame(Zeros)
toDataFrame = pandas.DataFrame.transpose(toDataFrame)
pt.plot (array)
pt.xlabel("time")
pt.ylabel("originalData")
pt.show()
pt.plot (B[1])
pt.xlabel("Number")
pt.ylabel("SurrogateOneIndex")
pt.show()

pt.plot (Zeros[1])
pt.xlabel("time")
pt.ylabel("SurrogateOne")
pt.show()

toDataFrame.to_excel("C:/Users/sarina/Desktop/surrogate/13.xlsx")
