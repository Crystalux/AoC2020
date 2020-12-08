import os.path
import re

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../input/day07.txt")

def append_value(dict_obj, key, value):
    # Check if key exist in dict or not
    if key in dict_obj:
        # Key exist in dict.
        # Append the value in list
        dict_obj[key].append(value)
    else:
        # As key is not in dict,
        # so, add key-value pair
        dict_obj[key] = [value]

rule = {}
reverse = {}
with open(path) as f:
    for line in f:

        bag, content = line.strip('.\n').split(" bags contain ")
        if content == 'no other bags':
            rule[bag] = []
        else:
            content_list = content.split(', ')
            bag_contains = []

            for item in content_list:

                item1 = list(re.findall(r'(\d{1,}) ([\w ]*) bag(?:s)?', item)[0])
                item1[0] = int(item[0])
                bag_contains.append(item1)
                append_value(reverse, item1[1], bag) 
            rule[bag] = bag_contains



def partA(color:str) -> int:
    contains_color = reverse[color]
    checked = set()
    for i in contains_color:
        if i not in checked:
            checked.add(i)
            if i in reverse:
                contains_color.extend(reverse[i])
    return len(checked)

def partB(color:str) -> int:
    count = 0
    contains_color = rule[color]
    for i in contains_color:
        n, m = i
        count += n + n*partB(m)
    return count

if __name__ == "__main__":
    print('PART A: ', partA('shiny gold'))
    print('PART B: ', partB('shiny gold'))
