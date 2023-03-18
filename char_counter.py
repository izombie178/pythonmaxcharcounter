string="d<jkbfkfbkfzbfkjvbfkvbzfvkjfbvkifbvzkvb3t38qt48343843q7rq8"
char_dict=dict()
max_occur=0
for char in string:
	if char.isalpha():
		if char in list(char_dict.keys()):
			char_dict[char]+=1
			if char_dict[char]>max_occur:
				index_max=char
				max_char=char
				max_occur=char_dict[char]
		else:
			char_dict[char]=0
print(char_dict)
print(max_char)
print(max_occur)
