from Armstrong import armstrong 
from Factorial import factorial
from Fibonacci import fibonacci
from Neon import neon
from Oddeven import oddeven
from Palindrome import palindrome
from Perfect import perfect
from Prime import prime
from Reverse import reverse
from Strong import strong  

print("Program Started")

while True:
    print("===== PYTHON NUMBER ANALYZER =====")
    print("1.Armstrong Number")
    print("2.Factorial Number")
    print("3.Fibonacci Number")
    print("4.Neon Number")
    print("5.Oddeven Number")
    print("6.Palindrome Number")
    print("7.Perfect Number")
    print("8.Prime Number")
    print("9.Reverse Number")
    print("10.Strong Number")
    print("0.Exit")
    choice=int(input("Enter your choice: "))   
    if choice==1:
        armstrong() 
        input("Press Enter to continue...")

    elif choice==2:
        factorial()
        input("Press Enter to continue...")

    elif choice==3:
        fibonacci()
        input("Press Enter to continue...")

    elif choice==4:
        neon()
        input("Press Enter to continue...")

    elif choice==5:
        oddeven()
        input("Press Enter to continue...")

    elif choice==6:
        palindrome()
        input("Press Enter to continue...")

    elif choice==7:
        perfect()
        input("Press Enter to continue...")

    elif choice==8:
        prime()
        input("Press Enter to continue...")

    elif choice==9:
        reverse()
        input("Press Enter to continue...")

    elif choice==10:
        strong()
        input("Press Enter to continue...")

    elif choice==0:
        print("Exit")
        break
    else:
        print("Its wrong Choice")
        input("Press Enter to continue...")

