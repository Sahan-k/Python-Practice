a=list(map(int,input("Enter the elements of the list separated by space:  ").split()))
largest=a[0]
second=a[0]
for i in range(1,len(a)):
  if a[i] > largest:
     second=largest
     largest=a[i]
  elif a[i] < largest and a[i]> second:
    second=a[i]
print(second)
