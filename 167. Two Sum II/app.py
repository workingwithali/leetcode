class sum(object):
    def TwoSum(self , arr, target):
        left , right = 0 , len(arr)-1
        while left < right:
            current = arr[left]+arr[right]
            if current == target:
                return [left+1, right+1]
            elif current < target:
                left +=1
            else:
                right -=1
        return []
sum = sum()
arr = [ 1,2,3,4,5,6,7,8,9]
target = 20
result = sum.TwoSum(arr,target)
print(result)