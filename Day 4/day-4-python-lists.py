# Python Lists = Data Structures that help organize and store data in python

# ie fruits = ["Cherry", "Apple", "Pear"]  // Similar to Arrays in JS

states_of_america = ["Delaware", "Pennsylvania", "Ohio", "Massachusetts"]
# list is in order from left to right in the list.
print(states_of_america[0]) # prints Delaware, the first state in the list
print(states_of_america[-1]) # counts back from the end of the list, would print Massachusetts.

states_of_america[1] = "Pencilvania"
print(states_of_america[1]) # changes "Pennsylvania" to "Pencilvania" by calling it by it's index [1]

states_of_america.append("Ryanland") # .append adds "Ryanland" to the end of the states_of_america list
print(states_of_america)

states_of_america.extend(["Other State", "Another State", "One more State"]) # .extend adds a bunch of items to the list, in the form of another list
print(states_of_america)