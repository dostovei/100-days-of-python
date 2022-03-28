# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen) #prints both nested lists in dirty dozen
print(dirty_dozen[0]) # prints fruits list in dirty dozen
print(dirty_dozen[1]) # prints vegetables list in dirty dozen

print(dirty_dozen[0][0]) # takes the 0 index nested list, fruits and then takes the 0 indexed item in the fruits list, which is strawberries