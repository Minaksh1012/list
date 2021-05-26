kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100] 
i=0
paisa=kitna_paisa_hai
counter=0
counter1=0
counter2=0
while i<len(paisa):
    if paisa[i]>10000000:
        counter+=1
    elif paisa[i]>100000 and paisa[i]<10000000:
        counter1+=1
    else:
        counter2+=1
    i+=1    
print(counter,"carorepati hai")
print(counter1,"lakapati hai")
print(counter2,"Dilwale hai")         








# 4 Crorepati hai
# 3 Lakhpati hai
# 4 Dilwale hai 










