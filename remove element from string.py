 
# mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
# subStr = "over" 
# Aapko aisa program likhna hai, jo subStr ki saari occurences ko mainStr se hata degi. Yaani uppar wale program ka output yeh hoga:

 
# the quick brown fox jumped the lazy dog. the dog slept the verandah. 


s="the quick brown fox jumped over the lazy dog. the dog slept over the verandah"
l=s.split()
i=0
while i<len(l):
    if l[i]=="over":
        i+=1
        continue
    print(l[i],end=" ")
    i+=1
