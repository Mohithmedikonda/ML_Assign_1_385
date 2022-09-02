import numpy as np

#ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#Sort the list and find the min and max age

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
#sorting the ages using sort function
ages

#sort function sorts the elements in the given data in ascending order by default.

#Add the min age and the max age again to the list#

ages.append(min(ages)) 
#Adding min ages to the ages#
ages.append(max(ages)) 
#Adding man ages to the ages#
ages

#min function shows the minimum value of the given elements as output
#max function shows the maximum value of the given elements as output

#Find the median age (one middle item or two middle items divided by two)#

np.median(ages) 
#Using median function to find the middle item#

#median function is used to calculate the median value of the given data

#Find the average age (sum of all items divided by their number)#

np.average(ages) 
#Using average function to find the average age#

#average function is used to calculate the average value of the given data

#Find the average age (sum of all items divided by their number)#

np.average(ages) 
#Using average function to find the average age#

#average function is used to calculate the average value of the given data