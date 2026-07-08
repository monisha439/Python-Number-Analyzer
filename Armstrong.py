def armstrong():
    no=int(input("Enter your number:"))
    sum=0
    temp=no
    while no>0:
        rem=no%10
        sum=sum+rem**3
        no=no//10
    if temp==sum:
        print("It is Armstrong number")
    else:
        print("Not Armstrong number")
