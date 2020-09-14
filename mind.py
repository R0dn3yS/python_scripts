output1 = ""
output2 = ""

for x in range(1, 7, 1):
    output1 = output1 + "\n"
    for y in range(1, x, 1):
        output1 = output1 + str(y)

print(output1)

for x in range (6, 1, -1):
    output2 = output2 + "\n"
    for y in range (1, x, 1):
        output2 = output2 + str(y)

print(output2)