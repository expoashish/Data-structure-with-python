# Insertion sort is a simple sorting algorithm that builds the final 
# sorted array (or list) one item at a time.

data=[3,5,2,0,4]
for i in range(1,len(data)):
	k=i
	while (k>0 and data[k-1]>data[k]):
		(data[k-1],data[k])=(data[k],data[k-1])
		k=k-1
print(data)
