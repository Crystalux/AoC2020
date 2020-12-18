import os.path
import operator
import re


def parse():
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "../input/day18.txt")
    with open(path) as f1: 
        dat = [line.strip() for line in f1]
    return dat


def partA(data:list):
    ans = 0

    for line in data:
        infix = re.findall(r"[0-9]|\+|\*|\(|\)", line)
        queue = []
        stack = []
        for i in infix:
            if i.isdigit():
                queue.append(int(i))
            elif i in ('+', '*'):
                if stack ==[]:
                    stack.append(i)
                elif stack[-1] == '(':
                    stack.append(i)
                else:
                    op = stack.pop()
                    queue.append(op)
                    stack.append(i)
            elif i == '(':
                stack.append(i)
            else:
                while '(' != stack[-1]:
                    op = stack.pop()
                    queue.append(op)
                stack.pop()
        while stack != []:
            op = stack.pop()
            queue.append(op)
        
        out = []
        for i in queue:
            if i == '+':
                x,y = out[-2:]
                out.pop()
                out.pop()
                out.append(x+y)
            elif i == '*':
                x,y = out[-2:]
                out.pop()
                out.pop()
                out.append(x*y)
            else:
                out.append(i)
        ans += out[0]
    
    return ans
def partB(data:list):
    ans = 0

    for line in data:
        infix = re.findall(r"[0-9]|\+|\*|\(|\)", line)
        queue = []
        stack = []
        for i in infix:
            if i.isdigit():
                queue.append(int(i))
            elif i in ('+', '*'):
                while stack !=[] and stack[-1] != '(' and (i != '+' or stack[-1] != '*'):
                    op = stack.pop()
                    queue.append(op)
                stack.append(i)
            elif i == '(':
                stack.append(i)
            else:
                while '(' != stack[-1]:
                    op = stack.pop()
                    queue.append(op)
                stack.pop()
        while stack != []:
            op = stack.pop()
            queue.append(op)
        
        out = []
        for i in queue:
            if i == '+':
                x,y = out[-2:]
                out.pop()
                out.pop()
                out.append(x+y)
            elif i == '*':
                x,y = out[-2:]
                out.pop()
                out.pop()
                out.append(x*y)
            else:
                out.append(i)
        ans += out[0]
    
    return ans

if __name__ == "__main__":
    data = parse()
    part1 = partA(data)
    part2 = partB(data)
    print('PART A: ', part1)
    print('PART B: ', part2)
    