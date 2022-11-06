workdays=[]
for i in range(1,31):
    if (i%6!=0) & (i%7!=0):
        workdays.append(i)
workdays=set(workdays)

n = int(input("сколько партий?:"))

workpartsdays={}

for i in range(1,n+1):
    firstday=int(input("первый день для "+str(i)+" партии"))
    step=int(input("период между заб. для "+str(i)+" партии"))
    workpart=[]
    for j in range(1,31):
        if (j!=firstday) & (j&step!=0):
            workpart.append(j)
    workpart=set(workpart)
    workpartsdays=set(workpartsdays)
    workpartsdays = workpartsdays.union(workpart)


print(workpartsdays.intersection(workdays))