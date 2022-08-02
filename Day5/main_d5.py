# Calculate student avg from list of heights received via user input
total_heights = 0
student_heights = input("Enter the student heights (in inches), separated by a space, to return their average: \n").split()

for student in student_heights:
    total_heights += int(student)
#another way to type cast each element in the list:
""" for student in range(0, len(student_heights)):
    student_heights[student] = int(student_heights[student]) """

student_avg = round(total_heights/len(student_heights))

print(f"The student average height is: {student_avg} inches")

#Student Avg solution 2 - no len() allowed

total_heights = 0
num_students = 0
student_heights = input("Enter the student heights (in inches), separated by a space, to return their average: \n").split()

for student in student_heights:
    total_heights += int(student)
    num_students +=1

student_avg = round(total_heights/num_students)

print(student_avg)


#Calculate the Highest Score from a list of scores
# no using max() or min() functions

student_scores = input("Input a list of student scores").split()
for n in student_scores:
    student_scores[n] = int(student_scores[n])
print(student_scores)

highest = 0
for score in student_scores:
    if score > highest:
        highest = score
print(f"The highest score is: {highest}")

# Adding even numbers exercise
total = 0
for number in range(1, 101, 2):
    total += number
print(total)


#FizzBuzz

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)





