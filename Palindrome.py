def palindrome():
    no=int(input("Enter Your no:"))
    rev=0
    temp=no
    while no>0:
        rem=no%10
        rev=rev*10+rem
        no=no//10
    if temp==rev:
        print("It is palindrom Number")
    else:
        print("Not palindrom Number")


