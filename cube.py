##########################
#This code was created for fun and practice my low skill
##########################
import random
def name():
    #name = input("Hi, whats your name? ")
    text = "Hi , whats your name? "
    name = format_input(text,str)
    length = len(name)
    print("Hello {0}! Your name have {1} symbol".format(name,length))

def number():
    format_text = "The number {0} is in binary: {0:0>4b} and the last value is {1}"
    text = "Enter the int number: "
    number = format_input(text,int)
    length = len(str(number))
    if length == 1:
        print(format_text.format(number,int(number % 10)))
    if length == 2:
        print((format_text + ", {2}").format(number,int(number % 10),int(number % 100 / 10 )))
    if length >= 3:
        print((format_text + ", {2}, {3}").format(number,int(number % 10),int(number % 100 / 10 ),int(number % 1000 / 100)))
    else:
        pass
    return

def cube():
    text = "Enter the number of cube (1-6) you want to see, 7 to random choice or  >= 8 to see all: "
    value = format_input(text, int)
    if value == 7:
        value = random.randint(1, 6)
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
    cube_list = [c1,c2,c3,c4,c5,c6]
    wrong = ("Wrong enter")
    error = ("Error enter")
    try:
        if 0 <= value <= 6:
            print(cube_list[value - 1])
        elif value >= 8:
            print(c1 + c2 + c3 + c4 + c5 + c6)
        else:
            print(wrong)
    except:
        print(error)
    return

def format_input(text,exp_type):
    cond = True
    while cond == True:
        value = input(text)
        try:
            if len(str(value)) == 0:
                print("The input is empty")
            elif exp_type == int:
                value = int(value)
                cond = False
                return (value)
            elif exp_type == str:
                value = str(value)
                cond = False
                return (value)
            elif exp_type == float:
                value = float(value)
                cond = False
                return (value)
            else:
                print("The input type in code is wrong")
        except:
                print("The input is wrong. Type {} number".format(str(exp_type)))


name()
number()
cube()
