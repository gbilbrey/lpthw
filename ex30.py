people = 20
cars = 40
buses = 20

if cars > people:
	print "we should take the cars."
elif cars < people:
	print "we should not take the cars"
else:
	print "we cannot decide"

if buses > cars:
	print "That is too many busses"
elif buses < cars:
	print "Maybe we can take the buses"
else:
	print "We still cannot decide."

if people > buses:
	print "Alright, we'll just take the buses."
else: 
	print "Fine, let's stay home then."
	
if cars > people and cars > buses:
	print "Cars win."
else:
	print "Cars don't win"
	

