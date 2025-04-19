A= [9,8,7,3,5,1,2]

#initialising n
n= len(A)

#rearranging elements at each n/2, n/4 ... intervals
interval= n//2

while interval > 0:
    for i in range(interval, n):
        temp= A[i]
        j= i
        while j >= interval and A[j - interval] > temp:
            A[j]= A[j- interval]
            j -= interval
            
        A[j]= temp
    interval //= 2
    
print("Sorted Array")
print(A)