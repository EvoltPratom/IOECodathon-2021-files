import sys

x = "1 2 3 2 2 2 3 3"

x = x.split()
# x.sort(reverse=1)

a = 0
b = 0

count = {}
for i in x:
    if i not in count:
        count[i] = 0
    count[i] += 1

# count contains the count
aa = list(count.values())
aa.sort(reverse=1)

s = sum(aa[0:2])
print(s)
