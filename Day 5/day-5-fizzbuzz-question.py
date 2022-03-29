for number in range (1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
    #Divisible by 3 AND 5
  elif number % 5 == 0:
    #Divisible by 5
    print("Buzz")
  elif number % 3 == 0:
    #Divisible by 3
    print("Fizz")
  else:
    print(number)