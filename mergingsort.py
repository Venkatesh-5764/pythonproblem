list1=[]
list2=[]
n=int(input())
for i in range(1,n+1):
    p=int(input("enter list1 elements:"))
    list1.append(p)
    q=int(input("enter list2 elements:"))
    list2.append(q)
list1.sort()
list2.sort()
list_3=list1+list2
list_3.sort()
print(list_3)
