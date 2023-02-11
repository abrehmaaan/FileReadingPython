nums = []
ch = 'Y'
while ch == 'Y' or ch == 'y':
    nums.append(int(input("Enter number: ")))
    ch = input("Do you want to add another number? [Y/N]: ")[0]
result = ""
for num in nums:
    result += str(num)
print("Numbers: "+result)