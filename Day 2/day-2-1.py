#Data Types

#STRING
"Hello"
print("Hello"[4]) #prints o
# how to print the index of a string, index always starts at 0

#INTEGER (whole numbers)
print(123 + 345)

#FLOAT (numbers with decimal places)
3.14159

#BOOLEAN
True
False

# Type Error, Type Checking and Type Conversion
num_char = str(len(input("What is your name?\n"))) # you have to convert int to str, otherwise it will not concatenate.
print("Your name has " + num_char + " characters.")


a = str(123)
print(type(a))

#MATHEMATICAL OPERATORS
print(6 + 9)
print(6 - 9)
print(6 * 9)
print(6 / 9)
print(6 ** 9) #exponent

#PEMDAS APPLIES HERE, CALCULATES LEFT TO RIGHT
# ()
# **
# * /
# + -
print(3 / 3 * 3 + 3 - 3) # equals 3.0

#NUMBER MANIPULATION
print(int(8 / 3)) #instead of 2.6666666, it rounds down to just 2...we want to round UP

print(round(8 / 3, 2)) #rounds up to 2.67 by rounding to 2 decimal places

print(8 // 3) #Floor division, rounds to 2

result = 4 / 2 #divides 4 by 2
result /= 2 #divides 4 by 2 AGAIN
print(result) # = 1.0

#F STRINGS
score = 0
height = 1.8
isWinning = True
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")





# DAY 2-1 EXERCISE
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
# print(type(two_digit_number))
#two_digit_number is a string, have to convert it to an integer
two_digit_a = int(two_digit_number[0])
two_digit_b = int(two_digit_number[1])
two_digit_sum = two_digit_a + two_digit_b
# print(type(two_digit_sum))
print(str(two_digit_a) + " + " + str(two_digit_b) + " = " + str(two_digit_sum))