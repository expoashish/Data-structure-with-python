# Selection sort is an algorithm that selects the smallest element from an 
# unsorted list in each iteration and places that element at the beginning
#  of the unsorted list.

data = [2,4,0,1,5,5,3,6,7,3,-9,6,-8]
for i in range(len(data)):
	min_value = i
	for j in range(i+1,len(data)):
		if(data[j]<data[min_value]):
			min_value=j
	(data[i],data[min_value])=(data[min_value],data[i])
print(data)
