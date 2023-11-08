st=input("enter the string")
l=[]
for i in st:
        l.append(i)
k=[]
count=0
for j in range(len(l)-1):
    if(l[j]!=l[j+1] and l[j] not in k):
        count=count+1
        k.append(l[j])
print(k,count)
        
        
