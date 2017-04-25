print "You enter a dark  room wit two doors. Do you go through door #1 or door #2"

door = raw_input("> ")

if door == "1":
	print "There is a giant bear there eating cheescake.  What do you want to do?"
	print "1. Take the cake"
	print "2. Scream at the bear."
	
	bear = raw_input("> ")
	
	if bear == "1":
		print "Something snarky1"
	elif bear == "2":
		print "Something snarky2"
	else:
		print "Well doing %s is probably better than the other choices" % bear
if door == "2":
	print "You stare into the endless abyss at Cthluthus's retina."
	print "1. Option one for door 2."
	print "2. Option two for door 2."
	print "3. Option three for door 2."
	
	insanity = raw_input("> ")
	
	if insanity == "1" or insanity == "2":
		print "you survive, some stupid stuff about jello."
	else:
		print "You go insane."

else:
	print "You didn't enter 1 or 2 at the initial door choice."

		
	
	
	



