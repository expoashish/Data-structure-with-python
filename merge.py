def mergesort(data):
    if len(data)>1:
        mid=len(data)//2
        leftarray=data[:mid]
        rightarray=data[mid:]
        mergesort(leftarray)
        mergesort(rightarray)

        i=j=k=0
        while i<len(leftarray) and j<len(rightarray):
            if (leftarray[i]<rightarray[j]):
                data[k]=leftarray[i]
                i=i+1
            else:
                data[k]=rightarray[j]
                j=j+1
            k=k+1
        while i<len(leftarray):
            data[k]=leftarray[i]
            i=i+1
            k=k+1
        while j<len(rightarray):
            data[k]=rightarray[j]
            j=j+1
            k=k+1

data = [3,56,7,5,78,1,0,6,4,8]
mergesort(data)
print(data)