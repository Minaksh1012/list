
number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19] 
# sum=30
i=0
b=[]
while i<len(n):
    j=len(n)-1
    # sum=30
    while j>4:
        if number==n[i]+n[j]:
            b.append([n[i],n[j]])
        j-=1
    i+=1
print(b)       

