def mergeLists(list1, list2):
	new_lst = []
	i = 0
	while i < len(list1):
	    for item in list2:
		if list1[i] < item:
		    new_lst.append(list1[i])
		    new_lst.insert(i + 1, item)
		    i += 1

	print new_lst

mergeLists([1,5,3], [2, 7,4])
