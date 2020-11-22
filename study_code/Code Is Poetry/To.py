'''
Code is poetry
        ---By A sample programmer
'''

your_love = None
my_love = None

while 1:
    Boy_said = input("Just say yes or no:")
    Girl_said = input("Just say yes or no:")

    if Boy_said == "yes" and Girl_said == "yes":
        your_heart = "me"
        my_heart = "you"
        break
    else:
        print("You must say yes!")

if "me" in your_heart:
    your_love = True

if "you" in my_heart:
    my_love = True

if your_love and my_love:
    print("Love you forever")
