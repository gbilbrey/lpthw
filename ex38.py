ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait, there aren't 10 things in that string"

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana","Girl", "Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "adding: ", next_one
	stuff.append(next_one)
	print "there are %d items now" %len(stuff)

print "there we go: ", stuff

print "let's do some things with stuff."


print stuff[1]
print stuff[-1]
print stuff.pop()
print "xxx".join(stuff)
print "yyy".join(stuff[3:-1])


	





	
	

	




