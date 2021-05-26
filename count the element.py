# counting of numbers in list with for loop

char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"] 
a=char_list    
d=[]
# for i in range(len(a)):      #we take range 0 to len(a)
#     x=[]                     #then we take empty list
#     c=0                      #then take counter 
#     for j in range(len(a)):  #we take range o to len(a)
#         if a[i]==a[j]:       # if these condition is true index of a and index of j
#             c=c+1            # counter increament
#     x.append(a[i])           #append the value of 'a' and 'c' in x
#     x.append(c)        
#     if x not in d:           #if x not in d
#         d.append(x)          #apend the value of x in d
# print (d)                    #output

    

i=0
while i<len(a):
    x=[]
    c=0
    j=0
    while j in range(len(a)):
        if a[i]==a[j]:
            c+=1
        j+=1    
    x.append(a[i])
    x.append(c)
    # i+=1
    if x not in d:
        d.append(x)
    i+=1    
print(d)                











# # a - 6 times
# # n - 3 times
# # t - 2 times
# # x - 2 times
# # u - 1 times
# # g - 1 times 








