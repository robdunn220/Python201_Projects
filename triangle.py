width = int(raw_input("What is the width of the triangle? "))

x = 1
y = width

for i in range(width):
    while x < width + 1:
        print (' ' * ((y-1)/2)) + ('*' * x) + (' ' * ((width-1)/2))
        x = x + 2
        y = y - 2
