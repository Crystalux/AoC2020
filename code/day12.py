import os.path
import time
import math

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../input/day12.txt")
with open(path) as f1:  
    nav = [[line.strip()[0], int(line.strip()[1:])] for line in f1]

def rotate_origin_only(xy, angle):
    """Only rotate a point around the origin (0, 0)."""
    x, y = xy
    if angle == 90:
        cos = 0
        sin = 1
    elif angle ==180:
        cos = -1
        sin = 0
    elif angle ==270:
        cos = 0
        sin = -1
    else:
        cos = 1
        sin = 0
    xx = x * cos + y * sin
    yy = -x * sin + y * cos

    return xx, yy

def partA(data:list):
    curr_dir = 'E'
    manY = 0
    manX = 0
    for i in data:
        dirr, unit = i
        if dirr == 'N':
            manY += unit
        elif dirr == 'S':
            manY -= unit
        elif dirr == 'E':
            manX += unit
        elif dirr == 'W':
            manX -= unit
        elif dirr == 'F':
            if curr_dir == 'N':
                manY += unit
            elif curr_dir == 'S':
                manY -= unit
            elif curr_dir == 'E':
                manX += unit
            else:
                manX -= unit

        else:
            comp = ['N','E','S','W']
            comp_idx = comp.index(curr_dir)
            unit /= 90
            unit = int(unit)
            if dirr == 'R':
                turn = (comp_idx + unit) % 4
                curr_dir = comp[turn]
            else:
                turn = (comp_idx - unit) % 4
                curr_dir = comp[turn]
    
    return (abs(manX)+abs(manY))

def partB(data:list):
    posX = 0
    posY = 0
    wayX = 10
    wayY = 1
    for i in data:
        dirr, unit = i
        if dirr == 'N':
            wayY += unit
        elif dirr == 'S':
            wayY -= unit
        elif dirr == 'E':
            wayX += unit
        elif dirr == 'W':
            wayX -= unit
        elif dirr == 'F':
            posX += wayX * unit
            posY += wayY * unit

        else:
            if dirr =='R':
                wayX, wayY = rotate_origin_only((wayX, wayY), unit)
            else:
                wayX, wayY = rotate_origin_only((wayX, wayY), 360 - unit)
            
            
    return (abs(posX)+abs(posY))



if __name__ == "__main__":
    print(partB(nav))