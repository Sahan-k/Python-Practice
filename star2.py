#decreasing triangle
n=5
for i in range(1,n+1):
  for j in range(1,n-i+1):
    print("*",end='')
  print()


for i in range(1,n+1):
  for j in range(1,(n-i)+(n-i)+1+1):
    print("*",end='')
  print()

for i in range(1,n+1):
  for j in range(1,(n-i)+(n-i)+2+1):
    print("*",end='')
  print()

