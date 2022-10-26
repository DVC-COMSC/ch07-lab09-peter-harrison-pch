# ******************************
# Make your Code
# ******************************
names = input().split()

naiveminmax = [names[0], names[0]]
for name in names:
    if len(name) <= len(naiveminmax[0]):
        naiveminmax[0] = name
        continue
    if len(name) >= len(naiveminmax[1]):
        naiveminmax[1] = name

print(*naiveminmax)