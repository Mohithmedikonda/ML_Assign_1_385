it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Input details

#Find the length of the set it_companies

len(it_companies)

#Here len finds the number of companies present in it_companies key

#Add 'Twitter' to it_companies

it_companies.add('Twitter')
it_companies

#The output will have the Twitter added to the list of it_companies

#Insert multiple IT companies at once to the set it_companies
it_companies.update(['Wells Fargo', 'JP Morgan'])
it_companies

#Two new IT companies are added to the list of it_companies

#Remove one of the companies from the set it_companies

it_companies.remove('Wells Fargo')
it_companies

#Wells Fargo is removed from the list of it_companies

#What is the difference between remove and discard
#The difference between discard () and remove () method is, In discard () method, 
#if the element is not present in the set, it does not throw any exception, whereasin
#remove () method if the element is not present in the set, it throws an exception.

#Join A and B
A.union(B)

#union function joins two keys

#Find A intersection B

A.intersection(B)

#intersection function intersects two keys

#Is A subset of B

A.issubset(B)

#Displays True or False

#Are A and B disjoint sets

A.isdisjoint(B)

#Displays True or False

#Join A with B and B with A

A.union(B) and B.union(A)

#union function joins two keys

#What is the symmetric difference between A and B

A.symmetric_difference(B)

#symmetric function is used to get elements that are not in intersection.

#Delete the sets completely

del A
del B

#A and B sets get deleted.

#Convert the ages to a set 

set_ages = set(age)
set_ages

#converts the ages from list to set

#And compare the length of the list and the set

len(age),len(set_ages)

#Displays the compared output.