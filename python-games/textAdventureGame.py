print("\nAs you slowly open your eyes you see sunshine streeming in through the windows.\n'Where am I?' you say out loud. You hear the sounds of a forest outside.")
def story():
    print("To your left there is a shelf. The door is in front of you.\nAnd to your right there is a window.\n\n")
    print("Which way would you like to go?")
    print("1. Go left\n2. Go outside\n3. Look out the window")
    imput_1 = input(': ')
    #1 is go to the left
    if imput_1 == '1':
        print('You walk over to the shelf to inspect it.')
        print('There is an empty glass jar sitting on the top shelf. Below that you see a piece of paper\n\n')
        print('What would you like to do? ')
        print('1. Read the paper\n2. Go back')
        imput_2 = input(': ')
        if imput_2 == '1':
            print('As you take the paper off the shelf you hear a bird singing outside')
        elif imput_2 == '2':
            story()
    #2 is go to the door
    elif imput_1 == '2':
        print('You slowly walk to the door and open it')
        print('Outside the warm breeze is cool against your skin. \nYou turn your head to the left where you see a mountain range. To the right you can see the ocean')
        print('Which way would you like to go?')
        print('1. Start traveling torward the mountains\n2. Start traveling torward the ocean')
        imput_2 = input(': ')
        if imput_2 == '1':
            print('You decide to start travelling to the mountains where you hope you will find more people')

        if imput_2 == '2':
            print('As you begin walking torward the ocean your way is barred by what looks like a deadly jungle')
            print('What would you like to do?')
            print('1. Go back\n2. Continue at your own risk')
            imput_3 = input(': ')
    #3 is go to the window
    #THIS IS A DEAD END
    elif imput_1 == '3':
        print('You walk over to the window')
        print("'What a wonderful view' you say to yourself.\n\n")
        print('What would you like to do?')
        print('1. Go back')
        imput_2 = input(': ')
        if imput_2 == '1':
            story()
def main():
    story()
main()
