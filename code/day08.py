import os.path
import time
import operator
from copy import deepcopy

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../input/day08.txt")
with open(path) as f:  
    intcode = [line.strip().split() for line in f]


ops = { "+": operator.add, "-": operator.sub }

def partA(data:list) -> int:
    freq = {i:0 for i in range(len(data))}
    pos = 0
    acc =  0
    while max(freq.values()) < 2:
        
        curr_act, opp = data[pos]
        op = opp[0]
        val = int(opp[1:])

        if curr_act == 'nop':
            pos += 1
        elif curr_act == 'jmp':
            pos = ops[op](pos, val)
        elif curr_act == 'acc':
            pos +=1
            acc = ops[op](acc,val)
        freq[pos] += 1

    return acc

def partB(data:list):
    
    for i in range(len(data)):
        cmds = deepcopy(data)

        if data[i][0] == 'nop':
            cmds[i][0] = 'jmp'
        elif data[i][0] == 'jmp':
            cmds[i][0] = 'nop'

        # commands position visisted so far
        visisted_pos=set()
        
        pos = 0
        acc = 0
        while pos not in visisted_pos:
            visisted_pos.add(pos)
            if pos >=len(data):
                return acc
            curr_act, opp = cmds[pos]
            op = opp[0]
            val = int(opp[1:])

            if curr_act == 'nop':
                pos += 1
            elif curr_act == 'jmp':
                pos = ops[op](pos, val)
            elif curr_act == 'acc':
                pos +=1
                acc = ops[op](acc,val)




if __name__ == "__main__":
    start = time.time()
    print('PART A: ', partA(intcode))
    end = time.time()
    print('Time: ', end-start)
    print('='*20)
    start = time.time()
    print('PART B: ', partB(intcode))
    end = time.time()
    print('Time: ', end-start)
    