import os.path
import time

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../input/day09.txt")
with open(path) as f1:  
    num_list = [int(line.strip()) for line in f1]

def if_sum_exist(x:list, y:int)->bool:
    for i in x:
        if (y-i in x) and (y != 2*i):
            return True
    return False
            


def partA(data:list):
    for i in range(25, len(data)):
        check =  data[i-25: i]
        if not if_sum_exist(check, data[i]):
            return(data[i], i)

def bruteB(data:list, targ:int):
    for i in range(len(data)):
        for j in range(i+1, len(data)-1):
            if sum(data[i:j+1]) == targ:
                minx = min(data[i:j+1])
                maxx = max(data[i:j+1])
                return minx+maxx


if __name__ == "__main__":
    ansA, idx = partA(num_list)
    print(ansA)
    start = time.time()
    print(bruteB(num_list[:idx],ansA))
    end = time.time()
    print("Time: ", end-start)
