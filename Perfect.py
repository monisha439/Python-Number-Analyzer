def perfect():
    no=int(input("Enter your no:"))
    sum=0
    for i in range(1,no):
        if no%i==0:
            sum=sum+i
    if sum==no:
        print("It is Perfect Number")
    else:
        print("Not perfect Number")
