# Reversing a list using two-pointer approach
def reverse_list(arr):
	left = 0
	right = len(arr)-1
	while (left < right):
		# Swap
		temp = arr[left]
		arr[left] = arr[right]
		arr[right] = temp
		left += 1
		right -= 1

	return arr

arr = [76,88,99,44,29,100]
print(reverse_list(arr))
