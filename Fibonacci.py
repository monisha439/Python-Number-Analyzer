def fibonacci():
    no=int(input("Enter your no:"))
    a=0
    b=1
    while no>0:
        print(a)
        c=a+b
        a=b
        b=c
        no=no-1
