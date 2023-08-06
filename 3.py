# Calculator, takes two numbers, no dceimals, and prints them : added, multiplied, divided both ways, and subtracted

# Parrot - repeats what you type in, forever

# Da li je broj prost - HARD

def calc():
    a = int(input())
    b = int(input())
    print(f"The sum is {a+b}")
    print(f"The {a-b}")
    print(a*b)
    print(a/b)
    print(b/a)
    print(a%b)
    pass

def parrot():
    while True:
        parot = input()
        if parot == "STOP":
            break
        print(parot)
    pass

def prost():
    a = int(input())
    for i in range(2,a):
        if a%i == 0:
            print("nije prost")
            return
    print("prost")
    pass


def guess():
    print("The computer made a number. You have to guess it. Good luck!")
    import random
    x = random.randrange(1,20)
    while True == True :
        your = int(input())
    
        if x < your:

            print("too high")
        
        if x > your:
        
            print("too low")
        
       # if x - 10 < your:
        
        #    print("way too high!")
        
       # if x + 10 < your:
        
        #    print("way too low!")
        
        if x == your:
        
            break
    if x == your:
        print("Correct")

    pass

calc()