a=[10,1,2,3,4,10,1,2,3,4,10,1,2,3,4]
seen={}
mark1=0
mark2=0
maxlen=0
i=1
for x in a:
  if x in seen and i-seen[x]>maxlen:
    maxlen=i-seen[x]
    mark1=seen[x]
    mark2=i
  else:
    seen[x]=i
  i+=1

mark1-=1
mark2-=1
for j in range(mark1,mark2+1):
  print(a[j],end=' ')

#if the question for length of maximun subarray then 
print("\nMaxLength is: ",maxlen+1)