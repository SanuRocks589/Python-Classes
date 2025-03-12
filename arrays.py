import array as arr

array1 = arr.array("i", [1,2,2,3,4,2,5,3,2])
print("Original array" + str(array1))
print("Number of occureneces of 2 in array 1 :" + str(array1.count(2)))
array1.reverse()
print("The reverse order of array 1 :" + str(array1))