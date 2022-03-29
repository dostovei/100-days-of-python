# LOOPS


#for item in list_of_items:
    #Do something to each item


fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
  print(fruit) # loops through each item in the fruits list. creates variable fruit
  print(fruit + " Pie")
print(fruits) # since print(fruits) is outside of the for loop (not indented), it prints only once AFTER the for loop is completed.


# LOOPS INDEPENDENT OF LISTS
# RANGE FUNCTION
for number in range(1, 10):
    print(number)
# for number in range(1, 11, 3): # the 3 is the step function
#   print(number)

total = 0
for number in range(1, 101):
  total += number
print(total) #5050