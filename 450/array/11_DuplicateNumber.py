 #find the duplicate number
def findDuplicate(nums):
  slow,fast=0,0

  while True:
    slow=nums[slow]
    fast=nums[nums[fast]]
    if slow == fast:
      break
    
  slow2=0
  while True:
    slow=nums[slow]
    slow2=nums[slow2]
    if slow==slow2:
      break
    
  return slow
arr = list(map(int,input().split()))
n=len(arr)
print(findDuplicate(arr))
