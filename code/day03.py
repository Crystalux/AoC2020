import os.path

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../input/day03.txt")
with open(path) as f1:  
    geo = [list(line.strip()) for line in f1]

def slope(data: list, right : int, down : int):
    tree = 0
    col = len(data[0])
    moveRight = 1
    for i in range(down, len(data), down):
        if data[i][(moveRight*right)%col]=='#':
            tree += 1
        moveRight+=1
    return tree

def partB(data:list):
    s1 = slope(data, 1,1)
    s2 = slope(data, 3,1)
    s3 = slope(data, 5,1)
    s4 = slope(data, 7,1)
    s5 = slope(data, 1,2)

    return s1*s2*s3*s4*s5

if __name__ == "__main__":
    print("PART A: ", slope(geo, 3,1))
    print("="*20)
    print("PART B: ", partB(geo))