def binarysearch(data,search):
	first=0
	last=len(data)-1
	while first<=last:
		mid=first+(last-first)//2
		if data[mid]==search:
			return mid
		elif data[mid]< search:
			first=mid+1
		else:
			last=mid-1
	return -1

data=[1,2,3,5,7,9]
search=1
final=binarysearch(data,search)

if final !=-1:
	print("data founded")
else:
	print("Not founded")
