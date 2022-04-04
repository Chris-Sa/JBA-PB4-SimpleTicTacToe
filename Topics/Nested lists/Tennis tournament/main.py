
lines = int(input())

results = []
for i in range(1, lines+1):
    match = input()
    results.append(match.split())

winners = []
for result in results:
    if result[1] == 'win':
        winners.append(result[0])

print(winners)
print(len(winners))