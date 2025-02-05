my_str = input ("Enter string: ")
my_str = my_str.casefold()
rev_str = my_str[::-1]
if my_str -- rev_str:
      print ("The string is a palindrome string.")
else:
      print("The string is not a palindrome string.")