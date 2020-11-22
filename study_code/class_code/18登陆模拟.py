# username = 41906324
# password = 123
userTuple=(41906301,123)
myUsername = eval(input("Please enter your username:"))
if myUsername == userTuple[0]:
    myPassword = eval(input("Please enter your password:"))
    if myPassword == userTuple[1]:
        print("The password is correct!")
    else:
        print("The password is incorrect!")
else:
    print("Username not found!")
