maze = [
    [["n"],             ["n"],              ["n"]],
    [["n","s","e"],     ["w","s"],          ["n","s"]],
    [["s","e"],         ["e", "w"],         ["w","s"]]
]

curr_pos = [0,0]

def valid_dir(maze):
    x = curr_pos[1]
    y = curr_pos[0]
    valid = maze[y][x]
    out = "You can travel: "
    if "n" in valid:
        out += "(N)orth or "
    if "e" in valid:
        out += "(E)ast or "
    if "s" in valid:
        out += "(S)outh or "
    if "w" in valid:
        out += "(W)est or "
    out = out[:-4] + "."
    print(out)


def valid(s, maze):
    x = curr_pos[1]
    y = curr_pos[0]
    valid = maze[y][x]

    if s in valid:
        return True
    else:
        return False

valid_dir(maze)
while True:
    
    inp = input("Direction: ").lower()
    if valid(inp, maze):
        if inp == "n":
            curr_pos[0] += 1
        elif inp == "e":
            curr_pos[1] += 1
        elif inp == "s":
            curr_pos[0] -= 1
        else:
            curr_pos[1] -= 1
        if curr_pos == [0,2]:
            print("Victory!")
            break
        
    else:
        print("Not a valid direction!")
    valid_dir(maze)
