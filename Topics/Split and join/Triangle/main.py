height = int(input())

print(" " * (height -1) + "#")
space = height - 1
hash = 1
for i in range(0, height-1):
    space = space - 1
    hash = hash + 2

    print(" " * space + "#" * hash)