l=[]
n=int(input())
for i in range (1,n+1):
    b=int(input())
    l.append(b)
size=len(l)
count=0
for j in range(0,size-1):
    for k in range(1,size-1):
        for r in range(2,size-1):
                sum=l[j]+l[k]+l[r]
                if(sum==0):
                    count=count+1
                    print(l[j],l[k],l[r])
print("the combinations of triplet zero in this list is",+count,"combinations")
