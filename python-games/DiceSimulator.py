import random
import time
def loading():
    for i in range(7):
        print ("Rolling","*"*i)
        time.sleep(.3)

def roll():
    loading()
    number = random.randint(1,6)
    print("You roled a",number)
def main():
    roll()
    again = input('Would you like to roll again? ')
    if again == 'y':
        main()
    else:
        return
main()
