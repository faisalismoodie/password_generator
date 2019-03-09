import numpy as np

def pg(y,z,x):
    s=''
    a=np.random.randint(low=y,high=z,size=x)
    a=a.tolist()
    print("Your Password: ",end='')
    for y in a:
        y=chr(y)
        s=s+y
        print(y,end='')
    print("\n")
    w=input("Do you want to save this Password [y/n]?")
    if w=='y':
        log(s)
    else:
        print("Trying again -->>")
        pg(y,z,x)

def sub():  
    x=int(input("\nEnter the size of Password you want to generate:"))
    b=int(input("How Powerful you want your Password to be?\nPress [1]. for 'I don't care about the strength' Password\nPress [2]. for 'Give me something Okay Okay O_o!!' Password\nPress [3]. for 'Oh!!!! MY GOOOOOODDDDDDDDDD!!!' Password\n"))
    if(b==1):
        y,z=97,122
    elif(b==2):
        y,z=65,122
    elif(b==3):
        y,z=33,127
    elif(b>3):
        print("Sorry Wrong Input :(")
    pg(y,z,x)
    
def log(s):
    with open("log.txt",'a') as f:
        f.write(s+"\n")

print('\n******PASSWORD GENERATOR******\n')
n,s=True,''
while n==True:
    i=int(input("\n________MAIN MENU_________\nPress [0]. To Exit\nPress [1]. To Generate your password.\n"))
    if i==1:
        sub()
    else:
        print("Thank You for using PASSWORD GENERATOR")
        n=False
        continue