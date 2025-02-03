while True:
    ch=int (input ("Enter your choice:\n1.Fahrenheit\n2.Celsius\n3.Exit\n"))
    if ch==1:
         far= float(input("\nEnter the temperature in Fahrenheit: "))
         cel= (far - 32) * (5/9)
         print("\nThe temperature in Celsius is: (:.2f}°C".format(cel))
    elif ch==2:
         cel = float(input("\nEnter the temperature in Celsius: "))
         far = (cel * 9/5) + 32
         print("\nThe temperature in Fahrenheit is: {:.2f}°F".format(far))
    elif ch==3:
        break
    else:
         print("\nInvalid choice. Please enter 1, 2, or 3.")