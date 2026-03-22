n=int(input("Enter the size: "))
arr=[]
for i in range(n):
  x=int(input("Enter the elements: "))
  arr.append(x)
print(arr)
for i in range(n):
  for j in range(0,n-i-1):
    if arr[j]>arr[j+1]:
      arr[j],arr[j+1]=arr[j+1],arr[j]
print("The sorted Array is: ")
for i in range(n):
  print(arr[i],end=' ')
  