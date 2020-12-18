import os.path
import time
import math
import numpy as np

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../input/day10.txt")
with open(path) as f1:  
    adapters = [int(line.strip()) for line in f1]

def partA(data:list) -> int:
    data.sort()
    data.insert(0,0)

    dif1 = 0
    dif3 = 1

    for i in range(1, len(data)):
        if data[i]-data[i-1] == 1:
            dif1 +=1
        elif data[i]-data[i-1] == 3:
            dif3 +=1
        else:
            print('error')
            break
        
    return (dif1*dif3)

def num_perm(x:int):
    if x ==1:
        return 1

    elif x==2:
        return 2
    elif x == 3:
        return 4
    elif x ==4:
        return 7
    else:
        print('something else')




def partB(data:list):
    data.sort()
    data.insert(0,0)
    data.insert(len(data), max(data))
    group_sizes= []

    curr_group = []
    for i in range(1, len(data)):
        if data[i]-data[i-1] == 1:
            curr_group.append(data[i])
        elif data[i]-data[i-1] == 3:
            if len(curr_group) != 0:
                group_sizes.append(len(curr_group))
                curr_group=[]
        else:
            print('error')
            break
    if len(curr_group) != 0:
        group_sizes.append(len(curr_group))
    
    print(group_sizes)
    perm = []
    for i in group_sizes:
        perm.append(num_perm(i))

    return np.prod(perm)
if __name__ == "__main__":
    print(partB(adapters))
