x = int(input("Please enter your number :"))
for y in range(x):
    print(" "* (x - y) + "*" * (2 * y + 1))
