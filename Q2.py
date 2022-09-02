#Create an empty dictionary called dog#
#Add name, color, breed, legs, age to the dog dictionary#

dog = {
'name' : 'Goldie',
'color' : 'Gold',
'breed' : 'Golden Retriever',
'legs' : 'four',
'age' : '3 years'
}
#adding name, color, breed, legs, age keys to empty dictionary dog#
dog

#A new dictionary called dog is created with the necessary details

#Create a student dictionary and add first_name, last_name, gender, age, marital status,skills, 
#country, city and address as keys for the dictionary#
student = {
'first_name' : 'Mohi',
'last_name' : 'Medik',
'gender' : 'Male',
'age' : 22,
'marital_status' : 'married',
'skills' : ['Cinephile', 'multi-tasking'],
'city' : 'Denver',
'address' : 'Washington street'
} 
#adding first_name, last_name, gender, age, marital status,skills, country, city and address as keys for student dictionary#
student

#A new dictionary called student is created with the necessary details.

#Get the length of the student dictionary#

len(student)
#Using len fuction to find length of dictionary#

#Here len function is used to find out the length of the student dictionary

#Get the value of skills and check the data type, it should be a list#

print(student['skills'])
#printing the value of skills key from dictionary student# 
print(type(student['skills']))
#printing the type of skills key from dictionary student#

#Modify the skills values by adding one or two skills#

student['skills'].append('Self Confidence')
#Using append function to add one more value to key skills# 
student

#Get the dictionary keys as a list

student.keys()

#The expected output is all the keys that are present in the student dictionary will be shown

#Get the dictionary values as a list

student.values()

#The expected output is all the values that are present in the student dictionary will be shown