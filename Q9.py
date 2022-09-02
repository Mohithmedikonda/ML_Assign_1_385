#Write a program, which reads weights (lbs.) of N students into a list and convert these weights to 
#kilograms in a separate list using Loop. N: No of students

list = []
weight = []
no_of_students = int(input("Enter no of students: "))
print('\nEnter student weights in lbs:')
for i in range(0, no_of_students):
    list.append(int(input()))

for i in range(0, no_of_students):
    weight.append(round(0.453592 * list[i], 2))

print(weight)