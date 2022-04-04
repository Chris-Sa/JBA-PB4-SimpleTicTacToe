# put your python code here

seq = input().split()
num = input()

pos = ""
for i in range(0, len(seq)):
    if seq[i] == num:
        pos = pos + str(i) + " "

if pos == '':
    print("not found")
else:
    print(pos.rstrip())
