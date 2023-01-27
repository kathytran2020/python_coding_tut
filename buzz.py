def testfunction(x):
    output = ""
    if x % 3 == 0:
        output += "fizz"
    if x % 5 == 0:
        output += "buzz"
    print(output)

for x in range(1, 100):
    testfunction(x)
