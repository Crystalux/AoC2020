import os.path
from collections import defaultdict

def parse():
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "../input/day21.txt")
    food = {}
    food_list = []
    with open(path) as f1:
        for line in f1:
            line = line.strip()
            ingre, aller = line.split(' (contains ')
            ingredient = ingre.split(' ')
            allergen = aller[:-1].split(', ')
            food_list.extend(ingredient)
            for i in allergen:
                if i not in food:
                    food[i] = set(ingredient)
                else:
                    inter = set(ingredient).intersection(food[i])
                    food[i] = inter
    
    for i in sorted(food, key=lambda k: len(food[k])):
        item = next(iter(food[i]))
        for j in food:
            if i != j:
                food[j].discard(item)

    return food, food_list
def partA(allergen:dict, food:list):
    union = set()
    for value in allergen.values():
        union = union.union(value)
    count = 0
    for i in food:
        if i not in union:
            count += 1

    return count
def partB(allergen:dict):
    sortedAllergens =sorted(allergen.keys(), key=lambda x:x.lower())
    ans=[]
    for i in sortedAllergens:
        elem = allergen[i].pop()
        ans.append(elem)
    return ','.join(ans)
if __name__ == "__main__":
    allergen, food = parse()
    ans1 = partA(allergen, food)
    print(ans1)
    ans2 = partB(allergen)
    print(ans2)
