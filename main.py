# ******************************
# Make your Code
# ******************************
names = input().split()

naiveminmax = [names[0], names[0]]
for name in names:
    if len(name) < len(naiveminmax[0]):
        naiveminmax[0] = name
    if len(name) > len(naiveminmax[1]):
        naiveminmax[1] = name
    elif len(name) == len(naiveminmax[0]) and name < naiveminmax[0]:
        naiveminmax[0] = name
    elif len(name) == len(naiveminmax[1]) and name < naiveminmax[1]:
        naiveminmax[1] = name

print(*naiveminmax)

#print("a" < "b")
#print("Z" < "z")

# so wants ansii alphabetical ordering