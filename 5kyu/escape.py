# Task: Car Park Escape

def escape(carpark):
    for p in range(len(carpark)):
        if 2 in carpark[p]:
            park = carpark[p:]
    sour = park[0].index(2)
    if len(park) == 1:
        return [] if sour+1 == len(park[0]) else ["R" + str(len(park[0]) - sour - 1)]
    park[-1][-1] = 1
    result = []
    for inx in range(len(park)):
        floor = 1
        des = park[inx].index(1)
        if des < sour:
            result.append('L' + str(sour-des))
        elif des > sour:
            result.append('R' + str(des-sour))
        sour = des
        if inx+1 == len(park):
            break
        if "D" not in result[-1]:
            result.append('D' + "1")
        else:
            floor = floor + int(result[-1][-1])
            result[-1] = 'D' + str(floor)
    return result



'''
# Best Practice:

## 1
def escape(carpark):

    car, stairs, start, moves, x = -1, -1, -1, [], 0
    
    while x < len(carpark):
        line = ''.join(map(str, carpark[x]))                                                           # Use string to avoid troubles with absence of 1 or 2
        stairs = line.find("1")                                                                        # Search for stairs
        if start == -1: start = line.find("2")                                                         # Do this only while the car had not been found yet
        
        if start >= 0: car, start = start, -2                                                          # Car found, start moving the "car" and declare that the car has been already found (start = -2)
        
        if start == -2:
            if x == len(carpark)-1:                                                                    # Car is at ground level
                if car != len(carpark[x])-1: moves.append( "R" + str(len(carpark[x])-1-car) )          # Move the car to the exit if needed
                return moves
                
            moves.append( ["L", "R"][stairs-car > 0] + str(abs(stairs-car)) )                          # Archive the move needed
            car, comingFrom = stairs, x                                                                # Move the car to the stair, collect the current level
            while carpark[x][car] == 1: x += 1                                                         # Go down while stairs are present
            moves.append("D" + str(x-comingFrom))                                                      # Archive the whole descent
            
        else: x += 1

## 2
def escape(carpark):

    while 2 not in carpark[0]: carpark.pop(0)
    r, ground, pos = [], len(carpark) - 1, carpark[0].index(2)
    for f, floor in enumerate(carpark):
        stairs = floor.index(1) if f != ground else len(floor) - 1
        if stairs != pos:
            r, pos = r + ['RL'[stairs < pos] + str(abs(pos - stairs))], stairs
        if f != ground:
            r += [('D' + str(int(r.pop()[1:]) +1)) if 'D' in r[-1] else 'D1']
    return r        
'''