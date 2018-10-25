#by Jan Vicha
name = input("Hi, whats your name? ")
length = len(name)
print("Hello {0}! Yours name has {1} symbol".format(name,length))

cond = True
while cond == True:
    try:
        number = int(input("Enter the int number: "))
        print("The number {0} is in binary: {0:0>4b} and the last value is {1} ".format(number,int(number % 10)))
        cond = False
    except:
        print("The input is wrong. Type number")

def cube(value):
    cube = str("""
    +-------+
    | {}   {} |
    | {} {} {} |
    | {}   {} |
    +-------+
    \n
    """)
    c1 = ("Number 1" + cube.format(" ", " ", " ", "o", " ", " ", " "))
    c2 = ("Number 2" + cube.format(" ", "o", " ", " ", " ", "o", " "))
    c3 = ("Number 3" + cube.format(" ", "o", " ", "o", " ", "o", " "))
    c4 = ("Number 4" + cube.format("o", "o", " ", " ", " ", "o", "o"))
    c5 = ("Number 5" + cube.format("o", "o", " ", "o", " ", "o", "o"))
    c6 = ("Number 6" + cube.format("o", "o", "o", " ", "o", "o", "o"))
    wrong = ("Wrong enter")
    error = ("Error enter")

    value = int(value)
    try:
        if value == 1:
            print(c1)
        elif value == 2:
            print(c2)
        elif value == 3:
            print(c3)
        elif value == 4:
            print(c4)
        elif value == 5:
            print(c5)
        elif value == 6:
            print(c6)
        elif value == 7:
            print(c1 + c2 +c3 + c4 + c5 + c6)
        else:
            print(wrong)
    except:
        print(error)
    return

value = input("Enter the number of cube (1-6) you want to see, or 7 to see all: ")
value = (cube(value))
