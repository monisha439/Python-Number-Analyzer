def factorial():
    no=int(input("Enter your no:"))
    fact=1
    for i in range(1,no+1):
        fact=fact*i
    print("Factorial Number:",fact) 
    