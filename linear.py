# Linear search is the simplest searching algorithm that searches for an 
# element in a list in sequential order. We start at one end and check 
# every element until the desired element is not found.


data=[3,5,9,7,4,0,2]
search=10
temp=0

for i in range(0,len(data)):
	if (search==data[i]):
		temp=1
		print("data has been founded")
if (temp==0):
	print("data not found")



