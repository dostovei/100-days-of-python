# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# 🚨 Don't change the code above 👆


#Write your code below this row 👇
# print(len(student_heights)) CAN'T USE
# print(sum(student_heights)) CAN'T USE
  
heights_total = 0 # initialize variable to hold the sum of list elements
for height in student_heights: # iterate over the list
  heights_total += height # add current list element to the sum

students_total = 0 # initialize variable to hold sum of students
for student in student_heights:
  students_total += 1
heights_average = round(heights_total / students_total) # rounds up height_average

print(heights_average)
