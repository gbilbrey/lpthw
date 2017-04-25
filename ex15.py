# imports "argv" from sys module
from sys import argv

# takes the two entries in the command line (after "python")
# and breaks into two values: script and the filename
# filname will be used later
script, filename = argv


txt = open(filename)
print "Here's your file, %r" %filename
print txt.read()

# Don't forget to close the text !!!!
txt.close()

# print "Type your filename again:"
# file_again = raw_input ('> ')

# txt_again = open(file_again)
# print txt_again.read(5)


 
