# Bubble Sort is a simple algorithm which is used to sort a given
# set of n elements provided in form of an array with n number of 
# elements. Bubble Sort compares all the element one by one and sort 
# them based on their values.

data=[3,5,2,0,4]

for i in range(len(data)):
	for j in range(0,len(data)-1):
		if (data[j]>data[j+1]):
			(data[j],data[j+1])=(data[j+1],data[j])
print(data)
