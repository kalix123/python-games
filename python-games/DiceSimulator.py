import random
def roll():
    number = random.randint(1,6)
    print(number)
def main():
    roll()
    again = input('Would you like to roll again? ')
    if again == 'y':
        main()
    else:
        return
main()
