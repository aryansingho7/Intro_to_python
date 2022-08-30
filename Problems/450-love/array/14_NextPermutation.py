def nextPermutation( nums):
  N= len(nums)
  pivot=0

#find pivot 
  for i in range(N-1,0,-1):
    if nums[i-1]<nums[i]:
      pivot=i
      break
    if pivot==0:
      nums.sort()
      return
    
#find swap which first no. is >pivot
      swap=N-1
      while nums[pivot - 1]>= nums[swap]:
        swap-=1
#swap
        nums[swap], nums[pivot-1]=nums[pivot-1], nums[swap]

    #reverse from pivot
        nums[pivot:]= sorted(nums[pivot:])