def even_numbers(low, high):
	even_nos = []
	for item in range(low, high):
		if item % 2 == 0:
			print item
		even_nos.append(item)
	print even_nos