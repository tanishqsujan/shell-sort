n= int(input("Enter size of array: "))
#A= list(map(int, input("Enter elements of Array: ").split()))

A= []
for i in range(n):
    A.append(int(input("Enter element: ")))
interval= n//2

while interval > 0:
    for i in range(interval, n):
       temp= A[i]
       j=i
       while j >= interval and A[j - interval] > temp:
          A[j] = A[j - interval]
          j -= interval
            
       A[j]= temp
    interval //= 2
    
print("Sorted Array")
print(A)
            