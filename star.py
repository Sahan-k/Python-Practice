#n*n pattern
for i in range(0,5):
  for j in range(0,5):
    print("*",end='')
  print("") 

#n*n increasing i value number pattern
for i in range(1,6):
  for j in range(0,5):
    print(i,end='')
  print("") 

#n*n increasing j value pattern
for i in range(0,5):
  for j in range(1,6):
    print(j,end='')
  print("")

#right angle tringle
for i in range(1,6):
  for j in range(0,i):
    print("*",end='')
  print("")

for i in range(1,6):
  for j in range(0,i+1):
    print("*",end='')
  print("")

#odd number
for i in range(1,6):
  for j in range(1,i+(i-1)+1):
    print("*",end='')
  print("")

  #even number 
for i in range(1,6):
  for j in range(0,i+i):
    print("*",end='')
  print("")

