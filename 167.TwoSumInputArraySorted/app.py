class solution :
    def TwoSum(self, numbers, target):
        l, r = 0, len(numbers) - 1
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum > target:
                r -=1
            elif sum < target:
                l +=1
            else:
                return [l + 1, r + 1]

solution = solution()
numbers = [1,2,3,4,5,6,7]
target = 9
result = solution.TwoSum(numbers, target)
print(result)
