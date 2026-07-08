def prime():
    no = int(input("Enter your number: "))
    count = 0

    if no <= 1:
        print("Not Prime Number")
    else:
        for i in range(2, no):
            if no % i == 0:
                count = count + 1

        if count == 0:
            print("It is Prime Number")
        else:
            print("Not Prime Number")
