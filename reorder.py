l=[]
n=int(input("enter no of elements do you want"))
for i in range (0,n):
    b=int(input("num:"))
    l.append(b)
print(l)
l2=[]
l3=[]
if(len(l)%2==0):
    for i in range(0,len(l)//2):
        l2.append(l[i])
        l2.append(l[-i-1])
else:
    for j in range(0,(len(l)+1)//2):
        l2.append(l[j])
        l2.append(l[-j-1])
for i in l2:
    if(i not in l3):
        l3.append(i)
print(l3)
            
    

            
    
