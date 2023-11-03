# On a plane, so I decided to do this

i: int = 0
x: int = 0
empty_list: str = []

while i < 1:
    while x < 101:
        empty_list += [x]
        x += 1
    i += 1

#print(empty_list)

y: int = 0

#print(sorted(empty_list))

n: int = 6

if n < 4:
    print("D")
else:
    if n > 1:
        print("C")
    else:
        print("A")
if n + 1 < 8:
    print("B")

idk: list[str] = ['hey', 'b', 'c', 'd']
print(len(idk))