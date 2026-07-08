def neon():
    no=int(input("Enter your no:"))
    temp=no
    cu=no*no
    sum=0
    while cu>0:
        rem=cu%10
        sum=sum+rem
        cu=cu//10
    if temp==sum:
        print("It is Neon Number")
    else:
        print("Not Neon Number")
