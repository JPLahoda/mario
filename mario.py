n = int(input("What is the integer?"))

def leftPyramid():
    spaces = n - 1
    hashtags = 1
    while spaces >= 0:
        for i in range(0,spaces):
            print(end=" ")
        spaces -= 1
        for i in range(0,hashtags):
            print("#", end="")
        hashtags += 1
        print()

def isRange():
    if n >= 1 and n <= 200:
        return
    else:
        return False

while isRange() == False:
    n = int(input("Value must be between 1 and 8. What is the integer?"))

leftPyramid()
