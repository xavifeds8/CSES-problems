n = int(input())
money = list(map(int, input().split()))
os = set()
temp = []
for i in money:
    if len(os) == 0:
        os.add(i)
        continue
    for j in os:
        temp.append(j+i)
    for k in temp:
        os.add(k)
    temp = []
    os.add(i)

print(len(os))
for i in sorted(os):
    print(i , end=" ")

