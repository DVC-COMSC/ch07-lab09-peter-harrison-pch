# ******************************
# Make your Code
# ******************************
names = input().split()

naiveminmax = [names[0], names[0]]
for name in names:
    if len(name) <= len(naiveminmax[0]) and name[0] < naiveminmax[0][0]:
        naiveminmax[0] = name
        continue
    if len(name) >= len(naiveminmax[1]) and name[0] < naiveminmax[1][0]:
        naiveminmax[1] = name

print(*naiveminmax)

#print("a" < "b")
#print("Z" < "z")

# so wants ansii alphabetical ordering