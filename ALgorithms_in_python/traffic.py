while True:
    try:
        x = input("Enter value: ")
        stop_light = int(x)
    except ValueError:
        print("Try Again")
    else:
        break

while stop_light <= 30:
    if stop_light >= 1 and stop_light < 10:
        print('Green light')
    elif stop_light < 20:
        print('Yellow light')
    elif stop_light < 30:
        print("Red light")
    stop_light += 1