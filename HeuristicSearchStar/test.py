from Search import AStarSearch


def SolveMaze():
    maze = [[0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 0]]

    start = [3, 0]  # starting position
    end = [4, 5]  # ending position
    cost = 1  # cost per movement
    search = AStarSearch()
    path = search.search(maze,cost, start, end)
    #print(path)
    for i in path:
        listel = []
        for j in i:
            if j >-1:
                listel.append("0")
            else:
                listel.append("X")
        print(listel)


SolveMaze()