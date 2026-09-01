import numpy as np
n=np.array(['Aarav','Diya','Kabir','Meera','Rohan','Ananya','Vikram','Ishita'])
m=np.array([[78,82,74],
           [92,88,95],
           [67,73,70],
           [85,91,89],
           [59,64,61],
           [95,90,93],
           [72,69,76],
           [88,84,86]])
a1=np.mean(m,axis=1)
a2=np.mean(m,axis=0)
for i in range(len(n)):
    print(n[i])
    print("Average:",a1[i])
print("Top performer:",n[np.argmax(a1)])
print("Python class avg:",a2[0])
print("Sql class avg:",a2[1])
print("Math class avg:",a2[2])
print("Students scoring 80+",n[a1>80])
    
  
