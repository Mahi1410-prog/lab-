
while True:
   print("1. Calculate the Average of the list.\n2.Exit\n")
   cho = int (input("Enter your choice: "))
   if cho == 1:
    lis = eval(input("\nEnter list of elements: "))
    average = sum(lis)/len (lis)
    print("\nAverage of the list -", average)
   elif cho==2:
    break
   else:
    print("\nInvalid Input!")