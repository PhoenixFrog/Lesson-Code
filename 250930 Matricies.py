string = input()
rows = string.split("/")
theMatrix = [newVar.split(" ")for newVar in rows]
print(theMatrix)

for i in range(len(theMatrix)):
    print(theMatrix[i][0])
