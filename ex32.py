the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list

for number in the_count:
	print "this is count %d" % number

# this also works for a list of strings
	
for fruit in fruits:
	print "this is fruit: %s" % fruit

# this also works for a mixed list:

for item in change:
	print "item from list: %r" % item

# we can also build a list.  Create an empty list first.

elements = range(0,6) #range returns a list

# then we use the "append" method to add to list

#for i in range(0,6):
#		elements.append(i)
#		print "adding %d to the list" % i

# now we can print out the list

for i in elements:
	print "element: %d" % i


		
	
	
	



