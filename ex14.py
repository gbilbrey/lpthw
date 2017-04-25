from sys import argv

script, username, fruit = argv
prompt = '--> '

print "Hi %s, I'm the %s script." %(username, script)

print "I'd like to ask you a few questions."
print "Do you like to eat %s?" % fruit
likes = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print '''
Alright, so you said %r about liking %r
and you have a %r computer. Nice.
''' %(likes, fruit, computer)

 
