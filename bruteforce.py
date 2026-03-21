def print_all_pairs(arr):
    #Print all possible pairs and its sum
    print("--All posiible Pairs and sum--")
    for i in range(len(arr)):
      for j in range(i+1,len(arr)):
        total=arr[i]+arr[j]
        print(f"{arr[i]} + {arr[j]}= {total}")
    print("")

def find_two_sum(arr,target):
  #find the pair of 2 elements that equal the target sum
  print(f"Pair that equal {target}")
  for i in range(len(arr)):
    for j in range(i+1,len(arr)):
      if(arr[i]+arr[j]==target):

        print(f"Match found: {arr[i]},{arr[j]}")
  print("")

def find_three_sum(arr,target):
  #find the triplets of 3 elements that equal the target sum
  print(f"Triplet that equal to {target}")
  for i in range(len(arr)):
    for j in range(i+1,len(arr)):
      for k in range(j+1,len(arr)):
        if(arr[i]+arr[j]+arr[k]==target):

          print(f"MAtch found: {arr[i]},{arr[j]},{arr[k]}")
  print("")

#Execution
nums=[10,20,30,40,50,60,70]
#call each function
print_all_pairs([10,20,30,40])
find_two_sum(nums,60)
find_three_sum(nums,60)