import pandas as pd
data={"Name":['Aarav','Diya','Kabir','Meera','Rohan','Ananya','Vikram','Ishita'],"Python":[78,92,67,85,59,95,72,88],
      "Sql":[82, 88, 73, 91, 64, 90, 69, 84],"Math":[74, 95, 70, 89, 61, 93, 76, 86]}
df=pd.DataFrame(data)
n=df["Name"]
df["Average"]=df[["Python","Sql","Math"]].mean(axis=1)
a=df["Average"]
for i in n:
    print(i)
    print("Average:",df[df["Name"]==i]["Average"].iloc[0])
print("Top performer:",df[a==max(a)]["Name"].iloc[0])
print("Python class avg:",df["Python"].mean())
print("Sql class avg:",df["Sql"].mean())
print("Math class avg:",df["Math"].mean())
print("Students scoring 80+",*df[a>80]["Name"],sep="\n")
    
