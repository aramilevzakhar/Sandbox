import re


# file = open('input.html', 'r').read()


# re.findall(r'\w{5}-\w{5}-\w{5}-\w{5}-\w{5}', file)
# print(file.read())


# file.close();

with open('input.html', 'r') as fo:
	tx = fo.read()
	collections = re.findall(r'\w{5}-\w{5}-\w{5}-\w{5}-\w{5}', tx)
	for i, item in enumerate(collections):
		print(i, item)
	# print(collections)

# print(file.read())