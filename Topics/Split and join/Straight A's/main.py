# put your python code here

grades = input().split()
# print(grades)
num = len(grades)
#print(num)
num_a = 0.0
for i in grades:
    if i == "A":
        num_a += 1
#print(num_a)

print(round(num_a / num, 2))