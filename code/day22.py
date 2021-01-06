import os.path
from itertools import groupby
import numpy as np
import time

def parse():
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "../input/day22.txt")
    with open(path) as f1:
        dat = [line.strip() for line in f1]
    player1, player2 = [list(group) for k, group in groupby(dat, lambda x: x == "") if not k]
    player1 =[int(x) for x in player1[1:]]
    player2 =[int(x) for x in player2[1:]]
    return player1, player2

def partA(p1:list, p2:list):
    desc = sorted(p1 + p2, key=int, reverse=True)
    while p1 != [] and p2 != []:
        c1 = p1.pop(0)
        c2 = p2.pop(0)
        if c1 > c2:
            p1.extend([c1, c2])
        else:
            p2.extend([c2, c1])
    if p2!= []:
        return 'P2', np.dot(p2, desc)
    else:
        return 'P1', np.dot(p1, desc)

def partB(p1:list, p2:list):
    p1_prev = []
    p2_prev = []
    while p1 != [] and p2 != []:
        
        if any(i == p1 for i in p1_prev) and any(i == p2 for i in p2_prev):
            return 'P1', p1
        else:
            p1_prev.append(p1.copy()), p2_prev.append(p2.copy())

        c1 = p1.pop(0)
        c2 = p2.pop(0)
        if c1 <= len(p1) and c2 <= len(p2):
            player, score = partB(p1[:c1], p2[:c2])
            if player == 'P1':
                p1.extend([c1, c2])
            else:
                p2.extend([c2, c1])
        else:

            if c1 > c2:
                p1.extend([c1, c2])
            else:
                p2.extend([c2, c1])

    if p2!= []:
        return 'P2', p2
    else:
        return 'P1', p1


if __name__ == "__main__":
    p1, p2 = parse()
    desc = sorted(p1+p2, key=int, reverse=True)
    print('REGULAR COMBAT')
    start1=time.time()
    player, ans1 = partA(p1.copy(), p2.copy())
    end1=time.time()
    print(player, ' WINS!')
    print(ans1)
    print('TIMER: ', end1-start1, 's')

    print('='*20)
    
    print('RECURSION COMBAT')
    start2=time.time()
    game2, ans2 = partB(p1, p2)
    end2=time.time()
    print(game2, ' WINS!')
    print(np.dot(ans2, desc[:len(ans2)]))
    print('TIMER: ', end2-start2, 's')