line, upper, lower = str(input()), 0, 0

for i in line: 
    if i.isupper(): 
        upper += 1 
    else:
        lower += 1

if upper > lower:
    print(line.upper())
else:
    print(line.lower())
