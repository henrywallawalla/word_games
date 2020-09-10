"""
with open("scrabble.txt", 'r') as f:
	count = 0
	for line in f:
		if count > 5:
			break
		print(line)
		count += 1
"""
def value(word):
	my_dict = 	{'a':1,"b":3,"c":3,"d":2,'e':1,'f':4,'g':2,'h':4,'i':1,'j':8	,'k':5,'l':1,'m':3,'n':1,'o':1,'p':3,'q':10,'r':1,'s':1,'t':	1,'u':1,'v':4,'w':4,'x':8,'y':4,'z':10}
	value = 0
	for character in word:
		value += my_dict[character]
		print(character)
		print(my_dict[character])
	print(value)