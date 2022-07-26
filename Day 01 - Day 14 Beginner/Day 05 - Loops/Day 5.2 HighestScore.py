'''
Write a program that calculates the highest score from a List of scores.

e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

Important you are not allowed to use the max or min functions. The output words must match the example. i.e

The highest score in the class is: x
'''

#Don't change the code below
from mailbox import MaildirMessage

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# Don't change the code above

#Write your code below
maximum = 0

for score in student_scores:
    if score > maximum:
        maximum = score

print(f"Highest score in the class = {maximum}")