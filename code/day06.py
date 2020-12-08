import os.path


my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../input/day06.txt")

ans =[]

with open(path) as f1:
    group = []
    for lines in f1:
        line = lines.strip()
        if len(line)<1:
            ans.append(group[:])
            group.clear()
        else:
            group.append(line)

    if len(group)!=0:
        ans.append(group)

def day06(data:list) -> type(None):
    union_yes = 0
    inter_yes = 0
    for x in data:
        union =  set(x[0]).union(*x)
        union_yes += len(union)

        inter = set(x[0]).intersection(*x)
        inter_yes += len(inter)

    print('PART A: ', union_yes)
    print('='*20)
    print('PART B: ', inter_yes)
    return None

if __name__ == "__main__":
    day06(ans)