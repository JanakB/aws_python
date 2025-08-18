import random
x=0
y=0
# random numbers from 0 to 99 20 times
for i in range(10):
    random_number = int(random.random()*100)
    print(random_number)

# if random number is in range 0 to 24 (X,Y) = (X, Y+1)
    if random_number in range(0, 24):
        y=y+1
        print("forward")
# if random number is in range 25 to 49 (X,Y) = (X, Y-1)
    elif random_number in range(25, 49):
        y=y-1
        print("backward")
# if random number is in range 50 to 74 (X,Y) = (X-1, Y)
    elif random_number in range(50, 74):
        x=x-1
        print("left")
# if random number is in range 75 to 99 (X,Y) = (X+1, Y)
    elif random_number in range(75, 100):
        x=x+1
        print("right")
print("x=", x, "y=", y)