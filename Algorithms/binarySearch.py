def binary_search(lst, itm):
	low = 0
	high = len(lst)-1

	while low <= high:
		mid = (low + high)//2
		guess = lst[mid]
		if guess == itm:
			return mid
		if guess > itm:
			high = mid - 1
		else:
			low = mid + 1

	return None

if __name__ == '__main__':
	my_lst = [1, 3, 5, 7, 9]

	print(binary_search(my_lst, 3)) # => 1
	print(binary_search(my_lst, -1)) # => None