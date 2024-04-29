def sequential_search(golfscore, target):
    for i in range(len(golfscore)):
        if golfscore[i]==target:
            return i 
    return -1

golfscore = []

g = 1

while g <= 100:
    golfscore.append(g)
    g = g+1

print(golfscore)

target = int(input("Enter number: "))
index = sequential_search(golfscore, target)

if index != -1:
    print("The target was found at index", index)
else:
    print("The target was not found")