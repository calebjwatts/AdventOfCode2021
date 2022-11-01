file = open("input.txt", "r")

# Turn each line to a number
depths = [int(line) for line in file.readlines()]

print(depths)

previousDepth = depths[0]
increased = 0
decreased = 0
same = 0

for depth in depths[1:]:
    if depth < previousDepth:
        print(f"{depth} (decreased)")
        decreased += 1
    elif depth > previousDepth:
        print(f"{depth} (increased)")
        increased += 1
    else:
        print(f"{depth} (same)")
        same += 1
    previousDepth = depth

print(f"Increased: {increased}")
print(f"Decreased: {decreased}")
print(f"Same: {same}")
file.close()