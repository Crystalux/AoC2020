import os.path
from copy import deepcopy
import time

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../input/day11.txt")
with open(path) as f1:  
    seat_layout = [list(line.strip()) for line in f1]


def adj_cells_count(data:list, xpos:int,ypos:int):
    occ = 0
    for y in range(-1,2):
        for x in range(-1,2):
            
            if x==0 and y==0: #current position
                continue
            y_check = y + ypos
            if y_check < 0 or y_check>=len(data):
                continue
            x_check = x + xpos
            if x_check < 0 or x_check>=len(data[0]):
                continue
            if data[y_check][x_check] =='#':
                
                occ += 1
    return occ
    

def running_grid(data:list, max_neigh:int, search_neighbour):
    prev_grid = deepcopy(data)
    curr_grid = deepcopy(data)

    while True:
        for i in range(len(prev_grid)):
            for j in range(len(prev_grid[0])):
                num_occ = search_neighbour(prev_grid, j, i)
                if prev_grid[i][j] == 'L' and num_occ == 0:
                    curr_grid[i][j] = '#'
                elif prev_grid[i][j] == '#' and num_occ > max_neigh:
                    curr_grid[i][j] = 'L'
                else:
                    curr_grid[i][j] = prev_grid[i][j]

        if curr_grid == prev_grid:
            return curr_grid
        else:
            old_prev_grid = prev_grid
            prev_grid = curr_grid
            curr_grid = old_prev_grid
    return None

def visible_seats(data:list, xpos:int,ypos:int):
    occ = 0
    for y in range(-1,2):
        for x in range(-1,2):
            
            if x==0 and y==0: #current position
                continue
            occ += look_dir(data, xpos, ypos, x,y)
    return occ

def look_dir(data:list, xpos, ypos, xdir, ydir):
    x = xpos + xdir
    y = ypos + ydir
    while x in range(len(data[0])) and y in range(len(data)):
        if data[y][x] == '#':
            return 1
        if data[y][x] == 'L':
            return 0
        x += xdir
        y += ydir
    return 0



def partA(data:list):
    stable = running_grid(data, 3, adj_cells_count)
    occupied = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if stable[i][j] == '#':
                occupied +=1
    return occupied

def partB(data:list):
    stable = running_grid(data, 4, visible_seats)
    occupied = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if stable[i][j] == '#':
                occupied +=1
    return occupied


if __name__ == "__main__":
    start = time.time()
    print('PART A: ', partA(seat_layout))
    end = time.time()
    print('TIMER A: ', end-start)

    print('='*20)

    start = time.time()
    print('PART B: ', partB(seat_layout))
    end = time.time()
    print('TIMER B: ', end-start)