import sys
import os

path = sys.argv[1]
os.chdir("/")

try:
    f = open(path, 'r')

except FileNotFoundError:
    print("Couldn't open the file\nChange directory or name. Make sure that file has .txt format.\n"
          "Then try again.")

except IsADirectoryError:
    print("Directory Error. Make sure that you put name of file at the end of your path.\n"
          "Example of input: '/home/../../filename.txt'")

else:
    count = 0
    for line in f:
        count += 1
    print(count)
    f.close()

