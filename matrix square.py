# 2 7 6
# 9 5 1
# 4 3 8
# is matrix square 


a=[]
# i=0
# for i in range (3):
#     b=[]
#     # j=0
#     for i in range(3):
#         j=int(input("enter the number"))
#         b.append(j)
#         # j+=1
#     a.append(b)
#     # i+=1
# print("matrix is.....")
# i=0
# for i in range(3):
#     for j in range(3):
#         print(a[i][j],end="  ") 
#     print()
# sumd1=0
# sumd2=0
# for i in range (3):
#     for j in range(3):
#         if i==j:
#             sumd1=sumd1+a[i][j]
#         if i+j==3-1:
#             sumd2=sumd2+a[i][j]    
# if sumd1!=sumd2:
#     f=1
# else:
#     for i in range (3):
#         sumr=0
#         sumc=0
#         for j in range (3):
#             sumr=sumr+a[i][j]
#             sumc=sumc+a[i][j]
#             if sumr!=sumd1:
#                 f=1
#             elif sumc!=sumd1:
#                     f=1
#             else:
#                     f=0

# if f==0:
#     print("matrix is magic square")
# else:
#     print("matrix is not magic square")    


                       
magic= [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
] 
sum=0
i=0
while i<len(magic):
    col=0
    while col<len(magic[i]):
        sum+=magic[i][col]
        col+=1
    j=0
    sum2=0
    while j<len(magic[i]):
        row=0
        while row<len(magic[i]):
            sum2+=magic[i][row]
            row+=1
        j+=1
    k=0
    sum3=0
    while k<len(magic[i]):
        dia=0
        while dia<len(magic[i]):
            sum3+=magic[i][dia]
            dia+=1
        k+=1
    i+=1
print(sum)
print(sum2)
print(sum3)
if sum==sum2==sum3:
    print("# ITS MAGIC SQUARE #")
else:
    print("its not magic square")                





