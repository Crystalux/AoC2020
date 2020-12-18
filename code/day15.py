from collections import defaultdict

test = [2,3,1]
inpA = [2,20,0,4,1,17]

def partA(lim:int, nums:list):
    seen=defaultdict(lambda: turn)
    prev = -1
    # add to seen dictionary
    for idx, num in enumerate(nums):
        seen[prev], prev = idx, num
    
    # edit 
    for turn in range(len(nums), lim):
        seen[prev], prev = turn, turn - seen[prev]
    
    return prev




if __name__ == "__main__":
    print(partA(2020, inpA))
    print(partA(30000000, inpA))