binary_num=[1,0,0,1,1,0,1,1]
value=0
for i in range (len(binary_num)):
  decimal=binary_num.pop()
  if decimal==1:
    value=value+pow(2,i)
print("the decimal number is",value)  
     
# binary_number=[1,0,0,1,1,0,1,1]
# # number=0
# value=0
# i=0
# while i<len(binary_number):
#     decimal=binary_number[len(binary_number)-i-1]
#     value=value+decimal*(2**i)
#     i=i+1
#     print(value)