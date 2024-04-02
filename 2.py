k = int(input())
nums = [int(x) for x in input().split()]
unique_nums = set()
for num in nums:
    if nums.count(num) > 1:
        continue
    if num % k % 2 != 0:
        unique_nums.add(num)
print(" ".join(str(x) for x in unique_nums))
