#Program to find intersection of two sorted arrays

#initialising two arrays
A1= [1,2,4,5,7,9]
A2= [0,2,3,4,7,8]

#initialising m and n
m= len(A1)
n= len(A2)

i,j = 0,0

while i < m and j < n:
    #comparing array items
    if A1[i] < A2[j]:
        i += 1
    elif A2[j] < A1[i]:
        j += 1
    else:
        #printing intersection of two array items
        print(A2[j], end= " ")
        j += 1
        i += 1