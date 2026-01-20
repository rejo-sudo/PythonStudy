#sort()

#it sorts the list in order and by default it list the orders in ascending order

nums = [4,9,0,1,2,8]

print(nums)
nums.sort()
print(nums)
print("sorted list of nums is -", nums)

nums.sort(reverse = True)# this paste the list in descending order
print("Descending order is -",nums)