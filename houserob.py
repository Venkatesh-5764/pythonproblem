l=[]
l2=[]
l3=[]
sum1=0
sum2=0
b=int(input("enter the number of houses"))
for i in range(0,b):
    num=int(input("house"))
    l.append(num)
for j in range(0,len(l),2):
    l2.append(l[j])
for k in range(1,len(l),2):
    l3.append(l[k])
for i in l2:
    sum1=sum1+i
for j in l3:
    sum2=sum2+j
if(sum1>sum2):
    print("the highest amount that can get robbed is",sum1)
else:
    print("the highest amount that can get robbed is",sum2)
    
    
