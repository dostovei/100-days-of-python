# DEBUG ODD OR EVEN
number = int(input("Which number do you want to check? "))

if number % 2 = 0: # Need ==, not =
  print("This is an even number.")
else:
  print("This is an odd number.")


# DEBUG LEAP YEAR
year = input("Which year do you want to check?") # year input needs to be an integer, correction: int(input("Which year do you want to check? "))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")


# DEBUG FIZZBUZZ
for number in range(1, 101):
  if number % 3 == 0 or number % 5 == 0: # number needs to be divisible by 3 AND 5, change 'or' to 'and'
    print("FizzBuzz")
  if number % 3 == 0: # needs to be elif statement
    print("Fizz")
  if number % 5 == 0: # needs to be elif statement
    print("Buzz")
  else:
    print([number]) # prints list called number, but we just want to print the number. correction: print(number)


  
  
