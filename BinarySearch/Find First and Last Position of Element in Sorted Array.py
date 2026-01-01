class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(nums,target,is_left_search):
            i = 0
            j = len(nums)-1
            idx = -1
            while i<=j:
                mid = i+(j-i)//2
                if nums[mid]==target:
                    idx = mid
                    if is_left_search:
                        j = mid-1
                    else:
                        i = mid+1
                elif nums[mid]<target:
                    i = mid+1
                else:
                    j = mid-1
            return idx
        start = binary_search(nums,target,True)
        end = binary_search(nums,target,False)
        return[start,end]
