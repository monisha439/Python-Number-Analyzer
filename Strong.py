def strong():
    no=int(input("Enter your no:"))
    sum=0
    temp=no
    while no>0:
        rem=no%10
        fact=1
        for i in range(1,rem+1):
            fact=fact*i
        sum=sum+fact
        no=no//10
    if temp==sum:
        print("It is Strong Number")
    else:
        print("Not Strong Number")
