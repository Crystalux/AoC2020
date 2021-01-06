import os.path
from collections import defaultdict
import numpy as np
import math

def parse():
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "../input/test.txt")
    tile_dict = {}
    border = {}
    with open(path) as f1: 
        tile_id = 0
        tile = []
        for line in f1:
            line = line.strip()
            if line[:4] == 'Tile':
                tile_id = int(line[5:-1])
            elif line == '':
                tile_dict[tile_id] = tile
                tile = []
            else:
                tile.append(line)
        tile_dict[tile_id] = tile
    
    for tile_id in tile_dict:
        tile = tile_dict[tile_id]
        up = tile[0]
        down = tile[-1]
        left = []
        right = []
        for i in tile:
            left.append(i[0])
            right.append(i[-1])
        forwards = [up, ''.join(right), down, ''.join(left)]
        backwards = [x[::-1] for x in forwards]
        border[tile_id] = forwards + backwards
    return tile_dict, border

def partA(borders):
    link = defaultdict(list)
    for i, (key1, value1) in enumerate(borders.items()):
        for j, (key2, value2) in enumerate(borders.items()):
            if j != i and not set(value1).isdisjoint(value2):
                link[key1].append(key2)

    corners = [k for k,v in link.items() if len(v) == 2]

    return np.prod(corners), link 

def build_gridId(link):
    size = int(math.sqrt(len(link)))
    gridId = np.empty([size, size], dtype=int)
    corners = [k for k,v in link.items() if len(v) == 2]
    edges = [k for k,v in link.items() if (len(v) == 3 or len(v) == 2)]
    i, j = 0,0
    while True:
        c1 = corners[0]
        gridId[i, j] = c1
        n1, n2 = link[c1]
        gridId[i, j+1] = n1
        gridId[i+1, j] = n2
        break
    print(gridId)


        

if __name__ == "__main__":
    tiles, border = parse()

    ans, connected = partA(border)
    print(ans)
    
    build_gridId(connected)
