import os.path
from functools import reduce

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../input/day13.txt")
with open(path) as f1: 
    dat = [[line.strip()] for line in f1]

start = int(dat[0][0])
buses = dat[1][0].split(',')

def partA(time:int, data:list):
    mins = 1000
    busId = 0
    for b in data:
        if b.isdigit():
            b = int(b)
            lapse = time % b
            if b-lapse < mins:
                mins = b-lapse
                busId = b
    return(mins * busId)
    
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def partB(data:list):
    n = []
    a = []
    for idx, busId in enumerate(data):
        if busId.isdigit():
            busId = int(busId)
            n.append(busId)
            a.append(-idx)
    return chinese_remainder(n, a)


if __name__ == "__main__":
    print("PART A: ", partA(start, buses))
    print('='*20)
    print("PART B: ", partB(buses))