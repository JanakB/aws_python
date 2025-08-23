def random_number(seed,num):
    if num ==0:
        return 1
    else:
        length = len(str(seed))
        start = int(length/2)
        end = int(length/2) * 3
        square = int(seed) * int(seed)
        if(len(str(square)) < 2*length):
            my_string = str(square)
            square = my_string.zfill(2*length)

        mid_term = str(square)[start:end]
        print(mid_term)
        random_number(mid_term, num-1)

seed = int(input("enter even digits number:"))
num = int(input("How many randon number you want?"))
random_number(seed, num)