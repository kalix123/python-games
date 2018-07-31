import random
import time

youtuber = {
'name': 'fill',
'content': 'games', # adding a comment here
'videos': 1,
'total_views': 0,
'subscribers': 0
}
youtuber['videos'] = 0
youtuber['subscribers'] = 0

def start():
    print('Welcome to Youtube')
    name = input('What would you like your channel to be called? ')
    youtuber['name'] = name
    content = input('What type of videos will you make(ex. Gaming)? ')
    youtuber['content'] = content
    print('\n')
    print(f"Thanks for joining Youtube {name}!")
    first_video()

def first_video():
    first = input('What is the name of your first video? ')
    upload()
    first_video_views = random.randint(1,30)
    first_video_subs = random.randint(1,5)
    time.sleep(1)
    print("Your video just got",str(first_video_views),"views")
    time.sleep(1)
    print('You also got', str(first_video_subs),'subscribers.\n')
    youtuber['subscribers'] = youtuber['subscribers']+first_video_subs
    youtuber['total_views'] = youtuber['total_views']+first_video_views
    home()

def video():
    first = input('What is the name of your video? ')
    upload()
    if(youtuber['subscribers'] > 100):
        views = random.randint(100,500)
        subs = random.randint(10,60)
        print("Your video just got",str(views),"views")
        print("You also got",str(subs),"subscribers.\n")
        youtuber['subscribers'] = youtuber['subscribers']+subs
        youtuber['total_views'] = youtuber['total_views']+views
    else:
        views = random.randint(20,100)
        subs = random.randint(5,20)
        print("Your video just got",str(views),"views")
        print("You also got",str(subs),"subscribers.\n")
        youtuber['subscribers'] = youtuber['subscribers']+subs
        youtuber['total_views'] = youtuber['total_views']+views
    home()
def upload():
    for i in range(1,5):
        print("Uploading","*"*i)
        time.sleep(1)
    print('Upload Complete')
    youtuber['videos'] = youtuber['videos']+1

#chance of getting a shoutout and gaining 200 subscribers
def shoutout():
    chance = random.randomint(1,2)
    if (chance == 1):
        print('Your favorite youtuber just \nnoticed one of your comments and decided to shout you out')
        print('You gain 200 subscribers')
        youtuber['subscribers'] = youtuber['subscribers']+200
    else:
        return

def home():
    print('This is your home page. \nuse the command -help for help')
    while True:
        user_prompt = input(': ')
        if (user_prompt == '-help'):
            print('Help: Page 1')
            print('-info    Use this command to see information about your channel')
            print('-upload  Use this command if you would like to upload a new video')
        elif (user_prompt == '-info'):
            for i in youtuber:
                print (i,':',youtuber[i])
        elif(user_prompt == '-upload'):
            print('You are going to upload a video')
            video()

def main():
    start()
main()
