import os.path
import re

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../input/day02.txt")
part1data=[]
with open(path) as f1:  
    for line in f1:
        a = line.strip()
        b = (re.split(r" |\: |\-", a))
        b[0] = int(b[0])
        b[1] = int(b[1])
        part1data.append(b)

def partA(data:list):
    count = 0
    for item in data:
        minC, maxC, char, password =item
        num = password.count(char)
        if minC <= num <= maxC:
            count += 1
        
    return count

def partB(data:list):
    count = 0
    for item in data:
        pos1, pos2, char, password =item

        if ((password[pos1-1]==char) or (password[pos2-1]==char)) and (password[pos1-1] != password[pos2-1]) :
            count += 1
        
    return count

if __name__ == "__main__":
    print(partA(part1data))
    print(partB(part1data))