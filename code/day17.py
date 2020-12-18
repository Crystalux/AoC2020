import os.path
import time
from collections import defaultdict

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../input/day17.txt")
with open(path) as f1: 
    dat = [list(line.strip()) for line in f1]

def find_neighbours(coords, pos):
    xpos, ypos, zpos = pos
    active = 0
    for z in range(-1, 2):
        for y in range(-1,2):
            for x in range(-1,2):
                
                if x==0 and y==0 and z==0: #current position
                    continue
                z_check = z + zpos
                y_check = y + ypos
                x_check = x + xpos
                if (x_check, y_check, z_check) in coords:
                    if coords[(x_check, y_check, z_check)] == True:
                        active += 1
    return active

def add_inactive(coords, pos):
    xpos, ypos, zpos = pos
    for z in range(-1, 2):
        for y in range(-1,2):
            for x in range(-1,2):
                
                if x==0 and y==0 and z==0: #current position
                    continue
                z_check = z + zpos
                y_check = y + ypos
                x_check = x + xpos
                if (x_check, y_check, z_check) not in coords:
                    coords[(x_check, y_check, z_check)]


def partA(data: list):
    coords = defaultdict(bool)

    #Add first layer from input to coords list
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == '#':
                coords[(x,y,0)]=True
                add_inactive(coords, (x,y,0))

    
    update = coords.copy()
    for _ in range(6):
        for pos,val in coords.items():
            neighs = find_neighbours(coords, pos)
            if val and (neighs not in (2,3)):
                update[pos] = False
            elif not val and neighs == 3:
                update[pos] = True
                add_inactive(update, pos)
            else:
                update[pos] = val
        temp = coords
        coords = update
        update = temp
    ans = sum(map((True).__eq__, coords.values()))
    return ans
                
def find_4d_neighbours(coords, pos):
    xpos, ypos, zpos, wpos = pos
    active = 0
    for w in range(-1, 2):
        for z in range(-1, 2):
            for y in range(-1,2):
                for x in range(-1,2):
                    
                    if x==0 and y==0 and z==0 and w == 0: #current position
                        continue
                    w_check = w + wpos
                    z_check = z + zpos
                    y_check = y + ypos
                    x_check = x + xpos
                    if (x_check, y_check, z_check, w_check) in coords:
                        if coords[(x_check, y_check, z_check, w_check)] == True:
                            active += 1
    return active

def add_4d_inactive(coords, pos):
    xpos, ypos, zpos, wpos = pos
    for w in range(-1, 2):
        for z in range(-1, 2):
            for y in range(-1,2):
                for x in range(-1,2):
                    
                    if x==0 and y==0 and z==0 and w ==0: #current position
                        continue
                    w_check = w + wpos
                    z_check = z + zpos
                    y_check = y + ypos
                    x_check = x + xpos
                    if (x_check, y_check, z_check, w_check) not in coords:
                        coords[(x_check, y_check, z_check, w_check)]


def partB(data: list):
    coords = defaultdict(bool)

    #Add first layer from input to coords list
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == '#':
                coords[(x,y,0,0)]=True
                add_4d_inactive(coords, (x,y,0, 0))

    
    update = coords.copy()
    for _ in range(6):
        for pos,val in coords.items():
            neighs = find_4d_neighbours(coords, pos)
            if val and (neighs not in (2,3)):
                update[pos] = False
            elif not val and neighs == 3:
                update[pos] = True
                add_4d_inactive(update, pos)
            else:
                update[pos] = val
        temp = coords
        coords = update
        update = temp
    ans = sum(map((True).__eq__, coords.values()))
    return ans

if __name__ == "__main__":
    start1 = time.time()
    part1 = partA(dat)
    end1 = time.time()
    timeA = end1 - start1

    start2 = time.time()
    part2 = partB(dat)
    end2 = time.time()
    timeB = end2 - start2

    print('PART A: ', part1)
    print('PART B: ', part2)
    print('='*20)
    print("Time Part A: ", timeA)
    print("Time Part B: ", timeB)