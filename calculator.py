from statistical import *
from operants import *
print("this code can only add,subtract,multiply,divide,root,mean,fact")
print()
q = input("do you wish to continue ..answer(YES/NO): ")
if q == "yes":
    try:
        class calculator:
            def __init__(self,oprt,x,y):
                self.oprt = oprt
                self.x = x
                self.y = y
            def operants(self):
                if self.oprt == "add":
                    return add(self.x,self.y)      
                elif self.oprt=="sub":
                    return sub(self.x,self.y)
                elif self.oprt=="mult":
                    return mult(self.x,self.y)
                elif self.oprt=="div":
                    return div(self.x,self.y)    
                elif self.oprt=="root":
                    return root(self.x, self.y)
                elif self.oprt== "square":
                    return square(self.x, self.y)
                elif self.oprt=="cube":
                    return cube(self.x, self.y)
                else:
                    print("this operation is not available ...please restart the program") 
                    for i in (self.operants==None):
                        if self.operants == bool:
                            int(i)
                        break
        def call():
            print("format:add,subtraction as sub,division as div,multiply as mult,root,square,cube,mean,factorial as fact ") 
            oprt= input("enter your operation: ") #for addition,subtraction,multiplication,division input add,sub,mult,division respectively for your operation
            if oprt == "mean":
                mean()
            elif oprt == "fact":
                h = int(input("enter the number yu want to find the factorial of: "))
                result = fact(h)
                print(result)
            else:
                x = int(input("enter your first number:"))  
                y = int(input("enter your second number:"))
                z = calculator(oprt,x,y)
                print(z.operants())
        call()
    except:
        print("you made an error during computation of the operation")
        print()
        eye = input("do you want to restart the program(yes/no):  ")
        if eye== "yes":
            print()
            try:
                call()
            except Exception as e:
                print("you made another error" , e)
                call()
        else:
            print("thank you for your time")
else: 
    print("please wait for our latest design that has more functions")