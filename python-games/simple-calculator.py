import random
#return the sum of num1 and num2
def add(num1,num2):
    return num1 + num2
#subtract num2 from num1
def subtract(num1, num2):
    return num1 - num2
#multiply num1 one by num2
def multiply(num1, num2):
    return num1 * num2
#divide num1 by num2
def divide(num1, num2):
    return num1 / num2
#main function
def main():
        #get user input for operation to perform
        operation = input("What do you want to do? (+, -, *, /): ")
        #check if input matches a valid operation
        if(operation != "+" and operation != "-" and operation != "*" and operation != "/" and operation != "add" and operation != "sub" and operation != "multi" and operation != "div"):
            #invalid operation
            print("That was not a valid operator")
        #else do this
        else:
            #get integer input for 2 numbers
            var1 = int(input("Number 1: "))
            var2 = int(input("Number 2: "))
            #if you chose plus run the plus function
            if (operation == "+"):
                print(add(var1, var2))
            #if you chose subtract run the subtract function
            elif (operation == "-"):
                print(subtract(var1,var2))
            #if you chose multiply run the multiply function
            elif (operation == "*"):
                print(multiply(var1,var2))
            #if you chose divide run the divide function
            elif (operation == "/"):
                print(divide(var1,var2))
            else:
                print("I dont understand")
#run the main function
main()
