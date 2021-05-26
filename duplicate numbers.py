# finding duplicates number
n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11] 
uniques=[]
# for num in n:
#     if num not in uniques:
#         uniques.append(num)
# print(uniques)


i=0
while i<len(n):
    # uniques=[]
    if n[i]>1:
        if n[i] not in uniques:
            uniques.append(n[i])
        i+=1
print(uniques) 
# i+=1       
