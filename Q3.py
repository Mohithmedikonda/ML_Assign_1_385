#Create a tuple containing names of your sisters and your brothers 

S1 = ('Happy','George','Reddy')
#names of brother and sister
S1

#Join brothers and sisters tuples and assign it to siblings

sisters = ('Happy',)
brothers = ('George','Reddy')
siblings = sisters + brothers
#Joining the tuples and assigning it to sibings
siblings

#How many siblings do you have?

len(siblings)

#Here,length function finds the length of number of strings present in the siblings key.
#Hence it gives the output of number of siblings.

#Modify the siblings tuple and add the name of your father and mother and assign it to
#family_members

father = 'DON'
mother = 'QUEEN'
family_members = siblings + (father,mother)
#assigning the siblings and father, mother to family_members key
family_members
