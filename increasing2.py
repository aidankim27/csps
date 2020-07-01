size=input()
n=input()
n=n.strip()
n=n.split(" ")
nums=[]
maxnum=[]
for i in n:
    nums.extend([int(i)])

def compute(nums):
    step = 0
    for i in range(1, len(nums)):
        if nums[i-1] > nums[i]:
            step += nums[i-1] - nums[i]
            nums[i] = nums[i - 1]
    return step

print(compute(nums))