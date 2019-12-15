from random import randint

def reverseDir(d):
    return (d << 2 | d >> 2) & 15


def generateMaze(w, h, sp):
    print(
        "Generating " + str(w) + " by " + str(h) + " maze at starting point [" + str(sp[0]) + ", " + str(sp[1]) + "].")
    maze = [[0 for y in range(h)] for x in range(w)]
    spacesLeft = w * h
    stack = []
    stack.append([sp[0], sp[1]])
    i = 0
    while len(stack) > 0:
        cursor = stack[len(stack) - 1]
        x = cursor[0]
        y = cursor[1]
        # input("Stack size: "+str(len(stack))+" ["+str(x)+","+str(y)+"]")
        d = [1, 2, 4, 8]
        blocked = 1
        while blocked:
            move = d[randint(0, len(d) - 1)]
            lx = x
            ly = y
            # Swap Move==N to Move&N
            if (move & 1):
                lx = lx + 1
            elif (move & 2):
                ly = ly + 1
            elif (move & 4):
                lx = lx - 1
            elif (move & 8):
                ly = ly - 1
            if (not (lx >= w or lx < 0 or ly >= h or ly < 0 or maze[lx][ly])):
                maze[x][y] += move
                x = lx
                y = ly
                maze[x][y] += reverseDir(move)
                stack.append([x, y])
                spacesLeft -= 1
                if (((((w * h) - spacesLeft) / (w * h)) * 100) % 5 == 0):
                    print(str((((w * h) - spacesLeft) / (w * h)) * 100) + "% complete.")
                blocked = 0
            else:
                if (len(d) == 1):
                    stack.remove(cursor)
                    blocked = 0
                else:
                    d.remove(move)
    print("Finished generating maze.")
    return maze

m = generateMaze(10, 10, [1, 1])

print(m)
