import os.path

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../input/day01.txt")
with open(path) as f1:  
    part1data = [int(line.strip()) for line in f1]

def part1(data : list):
    for i in range(len(data)):
        for j in range(i+1,len(data)):
            if (data[i] + data[j] == 2020):
                print(data[i],data[j])
                return data[i] * data[j]
    return "none found"

def part2(data:list):
    for i in range(len(data)):
        for j in range(i+1,len(data)):
            for k in range(i+j+1, len(data)):
                if (data[i] + data[j] + data[k]== 2020):
                    print(data[i],data[j], data[k])
                    return data[i] * data[j] * data[k]
    return "none found"

if __name__ == "__main__":

    print("Part A: " + str(part1(part1data)))
    print("="*10)
    print("Part B: " +str(part2(part1data)))