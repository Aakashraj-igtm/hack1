Mickey = {}
Donald = {}
for x in range(1, 9):
    for y in range(1, 9):
        for z in range(1, 9):
            if x != y and y != z and x != z:
                try:
                    Mickey[tuple(sorted((x, y, z)))]
                except KeyError:
                    try:
                        Donald[(x, y)]
                        try:
                            Donald[(y, x)]
                        except KeyError:
                            Mickey[tuple(sorted((x, y, z)))] = (y, x)
                            Donald[(y, x)] = z
                    except KeyError:
                        Mickey[tuple(sorted((x, y, z)))] = (x, y)
                        Donald[(x, y)] = z


m, d = map(int,input().split())
for x in range(m):
    y = tuple(sorted(map(int,input().split())))
    print (Mickey[y][0], Mickey[y][1])
for x in range(d):
    y = tuple(map(int,input().split()))
    print(Donald[y])


