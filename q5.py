lines = []
while True:
    n = input()
    if n:
        lines.append(n.upper())
    else:
        break

for n in lines:
    print(n)