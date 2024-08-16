#if else ladder
#grade and mark
'''
A - 81-100
B - 61-80
C - 51-60
D - 41-50
F - below 40
'''
'''
score=int(input("Enter your score:"))
if (score>80):
    print("A Grade")
else:
    if(score>60):
        print("B Grade")
    else:
        if(score>50):
            print("C Grade")
        else:
            if(score>40):
                print("D Grade")
            else:
                print("F Grade")
print("Thank you")
            
'''               
#if elif else statement
'''
score=int(input("Enter your score:"))
if (score>80):
    print("A Grade")
elif(score>60):
     print("B Grade")
elif(score>50):
     print("C Grade")
elif(score>40):
     print("D Grade")
else:
     print("F Grade")
print("Thank you")
'''

#While Loop
'''
count=1 #initialise
while count<=10: #condition
    print(count)
    count+=1 #increment
print("Done")    

count=1
while count<=20:
    print(count)
    count+=1
print("Done")    

count=10
while count>=1:
    print(count)
    count-=1
print("Done")    
'''        
#control statements
#break-exit
#continue
'''
count=0
while count<5:
    count+=1
    if count ==3 :
        break
    print(count)
print("End")
'''
count =10
while count<=10:
    print(count)
    if count == 1:
        break
    count-=1
print("End")


