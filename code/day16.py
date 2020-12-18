import os.path
from collections import defaultdict

def parse():
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "../input/day16.txt")
    with open(path) as f1: 
        dat = [line.strip() for line in f1]

    size = len(dat) 
    idx_list = [idx + 1 for idx, val in 
        enumerate(dat) if val == ''] 
  
  
    conditions, mine, near = [dat[i: j] for i, j in
        zip([0] + idx_list, idx_list + 
        ([size] if idx_list[-1] != size else []))]
    
    mine = [int(x) for x in mine[1].split(',')]
    nearby = []
    for i in near[1:]:
        tickets = [int(x) for x in i.split(',')]
        nearby.append(tickets)

    rules = defaultdict(list)
    ranges =set()
    for line in conditions[:-1]:
        rulename, values = line.split(': ')
        for vals in values.split(' or '):
            idx1, idx2 = [int(x) for x in vals.split('-')]
            rules[rulename].extend(list(range(idx1, idx2+1)))
            ranges.add((idx1, idx2))
    
    return rules, mine, nearby, ranges
  
def partA(tickets, ranges):
    error = 0
    valid_tickets = []
    for ticket in tickets:
        for value in ticket:

            valid = False
            for lo, hi in ranges:
                if lo <= value <= hi:
                    valid = True
                    break
            if not valid:
                error += value
                break
        if valid:
            valid_tickets.append(ticket)
    return error, valid_tickets

def partB(my_ticket, validTickets, rules):
    possible = {i: set(rules.keys()) for i in range(len(validTickets[0]))}
    for ticket in validTickets:
        for idx, value in enumerate(ticket):
            for rule in rules:
                if value in rules[rule]:
                    continue
                else:
                    possible[idx].discard(rule)
    # sort indices by number of possible fields
    # remove field from other indices
    for i in sorted(possible, key=lambda k: len(possible[k])):
        rule = next(iter(possible[i]))
        for j in possible:
            if i != j:
                possible[j].discard(rule)
    #get fields starting with departure
    ans = 1
    for i in possible:
        if possible[i].pop().startswith('departure'):
            ans*=my_ticket[i]   
        
    return ans

if __name__ == "__main__":
    rules, my, oth, ranges = parse()
    error, valid = partA(oth, ranges)
    partBans = partB(my, valid, rules)
    print('PART A: ', error)
    print('PART B: ', partBans)
    