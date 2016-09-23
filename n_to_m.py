start_number = int(raw_input('Please type a number to start your range from: '))
end_number = int(raw_input('Please type a number to end your range on: '))

if start_number > end_number:
    start_number = int(raw_input("Please make your starting number smaller: "))

for number in range(start_number, end_number + 1):
    print number
