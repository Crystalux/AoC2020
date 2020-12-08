import os.path

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../input/day05.txt")
with open(path) as f1:  
    seats = [line.strip() for line in f1]
seat_id=[]
def seat(x:str) -> (int, int):
    row = list(range(128))
    for char in x[0:7]:
        midrow = int(len(row)/2)
        if char == 'F':
            row = row[:midrow]
        else:
            row = row[midrow:]
    
    col = list(range(8))
    for char in x[7:]:
        midcol = int (len(col)/2)
        if char == 'R':
            col = col[midcol:]
        else:
            col = col[:midcol]

    return(row[0],col[0])

def seatId(row:int, col:int) -> int:
    return row * 8+ col

def partA(data:list) -> int:

    for i in data:
        row, col = seat(i)
        seat_id.append(seatId(row,col))
    
    return max(seat_id)

def partB(data:list) -> int:
    max_id = max(seat_id)
    min_id = min(seat_id)
    for i in range(min_id, max_id+1):
        if i not in seat_id:
            return i

if __name__ == "__main__":
    print(partA(seats))
    print(partB(seat_id))