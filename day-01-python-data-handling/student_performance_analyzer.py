students = [
    {"name": "Aarav", "python": 78, "sql": 82, "math": 74},
    {"name": "Diya", "python": 92, "sql": 88, "math": 95},
    {"name": "Kabir", "python": 67, "sql": 73, "math": 70},
    {"name": "Meera", "python": 85, "sql": 91, "math": 89},
    {"name": "Rohan", "python": 59, "sql": 64, "math": 61},
    {"name": "Ananya", "python": 95, "sql": 90, "math": 93},
    {"name": "Vikram", "python": 72, "sql": 69, "math": 76},
    {"name": "Ishita", "python": 88, "sql": 84, "math": 86}
]
print("Student performance analyzer")
a=[]
p=[]
s=[]
m=[]
h=[]
c=[]
for i in students:
    l=list(i.values())
    print(l[0])
    c.append(l[0])
    avg=(l[1]+l[2]+l[3])/3
    if avg>=80:
        h.append(l[0])
    a.append(avg)
    p.append(l[1])
    s.append(l[2])
    m.append(l[3])
    print("Average:",avg)
print('Top performer:',c[a.index(max(a))])
print('Python class average:',sum(p)/len(p))
print('Sql class average:',sum(s)/len(s))
print('Math class average:',sum(m)/len(m))
print("Students scoring 80+",*h,sep='\n')
  
