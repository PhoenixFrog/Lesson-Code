edges = [[0,1,0,1,0,0],
        [1,0,1,0,1,1],
        [0,1,1,1,1,0],
        [1,0,0,0,1,0],
        [0,1,0,1,0,0],
        [0,1,1,0,0,0]]
nodes =["A","B","C","D","E","F"]
for column in nodes:
    for row in nodes:
        if edges[nodes.index(column)][nodes.index(row)] == 1:
            print(f"{row} is connected to {column}")
