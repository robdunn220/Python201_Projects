height = int(raw_input("What is the height? "))
width = int(raw_input("What is the width? "))

if (height > 0) and (width > 0):
    print '*' * width
    for x in range(height):
        print '*' + (' ' * height) + '*'
    print '*' * width
