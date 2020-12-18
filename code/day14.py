import os
import re
import time

def partA():
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "../input/day14.txt")
    mask = ''
    memory = {}
    with open(path) as f1: 
        for line in f1:
            ln = line.strip()
            if ln.startswith('mask'):
                mask = ln[7:]
            else:
                temp = re.findall(r'\d+', ln)
                res = list(map(int, temp))
                value = '{0:036b}'.format(res[1])
                new_val = apply_mask(mask, value)
                memory[res[0]] = int(new_val, 2)

    return sum(memory.values())

def apply_mask(mask:str, value:str):
    new_val = []
    for i in range(len(mask)):
        if mask[i]!='X':
            new_val.append(mask[i])
        else:
            new_val.append(value[i])
    return ''.join(new_val)

def partB():
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "../input/day14.txt")
    mask = ''
    memory = {}
    with open(path) as f1: 
        for line in f1:
            ln = line.strip()
            if ln.startswith('mask'):
                mask = ln[7:]
            else:
                temp = re.findall(r'\d+', ln)
                res = list(map(int, temp))
                mem = '{0:036b}'.format(res[0])
                new_mem = apply_mem_mask(mask, mem)
                recurse_mem(new_mem,0,[],memory,int(res[1]))

    return sum(memory.values())

def apply_mem_mask(mask:str, value:str):
    new_val = []
    for i in range(len(mask)):
        if mask[i] == '0':
            new_val.append(value[i])
        else:
            new_val.append(mask[i])
    return new_val

def recurse_mem(mem:list, i:int, address:list, memory:dict, val:int):
    if i==36:
        memory[''.join(address)] = val
        return None
    if mem[i] == 'X':
        zero_add = address.copy()
        zero_add.append('0')
        one_add = address.copy()
        one_add.append('1')
        recurse_mem(mem, i+1, zero_add, memory, val)
        recurse_mem(mem, i+1, one_add, memory, val)
    else:
        address.append(mem[i])
        recurse_mem(mem, i+1, address, memory, val)

if __name__ == "__main__":
    start1 = time.time()
    part1 = partA()
    end1 = time.time()
    print('PART A: ', part1)
    print('TIME: ', end1-start1)

    print('='*20)
    start2 = time.time()
    part2 = partB()
    end2 = time.time()
    print('PART B: ', part2)
    print('TIME: ', end2-start2)
    #print(apply_mask('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', '000000000000000000000000000000001011'))