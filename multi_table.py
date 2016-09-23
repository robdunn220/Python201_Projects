multi_factor = int(raw_input("What do you want the table to be set to? "))

if multi_factor <= 0:
    multi_factor = int(raw_input("Please enter a factor greater than 0: "))

for x in range(1,multi_factor + 1):
    for y in range(1, multi_factor + 1):
        result = x * y
        print "%s X %s = %s" %(x, y, result)
