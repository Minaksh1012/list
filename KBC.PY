# question_list = [
#     "How many continents are there?",              # pehla question
#     "What is the capital of India?",            # doosra question
#     "NG mei kaun se course padhaya jaata hai?"    # teesra question
# ]

# options_list = [
#     #pehle question ke liye options
#     ["Four", "Nine", "Seven", "Eight"],
#     #second question ke liye options
#     ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
#     #third question ke liye options
#     ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
# ]

# # har ek question ke liye, uski solution key (yeh index nahi hai)
# solution_list = [3, 4, 1] 
# answer_list=[
#     ["(1)four","(3)seven"],
#     ["(1)chandigarh","(4)delhi"],
#     ["(1)software engineering","(3)Tourism"]

# ]
# print("KON BANEGA KRODPATI,(KBC)")
# i=0
# s=0
# count=0
# while i<len(question_list):
#     print(question_list[i])
#     a=0
#     b=i
#     while a<len(options_list[i]):
#         k=options_list[i][a]
#         print(a+1,k)
#         a=a+1
#         lifeline=input("DO YOU WANT LIFE LINE")
#         if lifeline=="yes":
#             print("YOUR USING 50-50 LIFE LINE")
#         if count<1:
#             print(answer_list[i])






# #     i+=1    question_list = [
# question_list=["How many continents are there?",              # pehla question
#     "What is the capital of India?",            # doosra question
#     "NG mei kaun se course padhaya jaata hai?"    # teesra question
# ]

# options_list = [
#     #pehle question ke liye options
#     ["Four", "Nine", "Seven", "Eight"],
#     #second question ke liye options
#     ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
#     #third question ke liye options
#     ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
# ]

# # har ek question ke liye, uski solution key (yeh index nahi hai)
# solution_list = [3, 4, 1] 
# answer_list=[
#     ["(1)four","(3)seven"],
#     ["(4)Delhi","(2)Bhopal"],
#     ["(4)Agricultue","(1)Software Engineering"]
# ]
# print("WELCOME TO KAUN BANEGA CROREPATI (KBC)")
# i=0
# s=0
# count=0
# while i<len(question_list):
#     print(question_list[i])
#     a=0
#     b=i
#     while a<len(options_list[i]):
#         k=options_list[i][a]
#         print(a+1,k)
#         a=a+1
        
# #     lifeline=input("DO YOU WANT 50 50 LIFELINE")
# #     if lifeline=="yes":
# #         print("50-50 lifeline")
# #         if count<1:
# # #             print(answer_list[b])
# #             num=int(input("enter your answer"))
# #             if num==solution_list[i]:
# #                 # s+=10000
# #                 print("answer is correct")
# #                 # print("you win Rs/",s)
# #             else:
# #                 print("your answer is wrong")
# #                 print("SORRY!you cant play again")
# #                 break
# #             count+1
# #         else:
# #             print("you already use 50-50 lifeline")
# #             # if m==solution_list[i]:
# #     else:
#         pass
    # i=i+1
#     # else:

question_list = [
    "How many continents are there?",              # pehla question
    "What is the capital of India?",            # doosra question
    "NG mei kaun se course padhaya jaata hai?"    # teesra question
]

options_list = [
    #pehle question ke liye options
    ["Four", "Nine", "Seven", "Eight"],
    #second question ke liye options
    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
    #third question ke liye options
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]

# har ek question ke liye, uski solution key (yeh index nahi hai)
solution_list = [3, 4, 1] 
answer_list=[
    ["(1)four","(3)seven"],
    ["(4)Delhi","(2)Bhopal"],
    ["(4)Agricultue","(1)Software Engineering"]
]
print("kaun Banega codepati (KBC)")
i=0
s=0
count=0
while i<len(question_list):
    print(question_list[i])
    a=0
    b=i
    while a<len(options_list[i]):
        k=options_list[b][a]
        print(a+1,k)
        a=a+1
    num1=input("do you want 50 50 lifeline")
    if num1=="yes":
        print("50 50 lifeline")
        if count<1:
            print(answer_list[b])
            num2=int(input("enter your answer"))
            if num2==solution_list[i]:
                s+=100000
                print("your answer is correct")
                print("you win Rs/",s)       
            else:
                print("incorrect answer")
                print("you can,t play again")
                print("you win Rs/",s)
                break
            count+=1
        else:
            print("you already use life line")
            num3=int(input("enter your answer"))
            if num3==solution_list[i]:
                s+=100000
                print("your answer is correct")
                print("you win Rs/",s)
            else:
                print("incorrect answer")
                print("you can,t play again")
                print("you win Rs/",s)
                break  
            
    else:
        pass
        num3=int(input("enter your answer"))
        if num3==solution_list[i]:
            s+=100000
            print("your answer is correct")
            print("you win Rs/",s)
        else:
            print("incorrect answer")
            print("you can,t play again")
            print("you win Rs/",s)
            # break  

    i+=1
print("COGRATULATIONS!!")
print("TOU WON THE TRIP FOR THREE TO AMERIKA WITH MONEY ",s)

   



