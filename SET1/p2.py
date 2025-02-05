
while True:
    l = float(input("Enter the length: "))
    b = float(input("\nEnter the breadth: "))
    print("\n1.Area\n2.Perimeter\n3.Exit")
    cho-int(input("\nEnter the choice: "))
    if cho == 1:
        area = 1*b
        print("\nArea of the rectangle with length", end="")
        print(1, "and breadth",b,"is: ",area)
    elif cho==2:
        per = 2*(1+b)
    elif cho==3:
        break
    else:
        print("Invalid Input!")