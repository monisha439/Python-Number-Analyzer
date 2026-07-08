def reverse():
    no=int(input("Enter Your no:"))
    rev=0
    while no>0:
        rem=no%10
        rev=rev*10+rem
        no=no//10
    print("Reverse Number",rev)
