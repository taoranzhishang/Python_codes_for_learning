import os

str1 = "hello"
str2 = "world"
print(str1 + " " + str2)

str3 = "\"C:\\Program Files (x86)\\Google\\Chrome\\Application\\"
str4 = "chrome.exe\""
print(str3 + str4)
os.system(str3 + str4)

num = 1
print("\"C:\\Program Files (x86)\\" + str(num) + ".txt\"")
