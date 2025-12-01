test = 50
actual = 50
zeros = 0

with open("day1_input.txt") as f:
    for line in f:
        direction = line[:1]
        distance = int(line.strip()[1:len(line)])
        
        if direction == 'R':
            test += distance
            if test > 99:
                actual = (actual + distance) % 100
                test = actual
            else:
                actual = test
                
        elif direction == 'L':
            test -= distance
            if test < 0:
                actual = (actual - distance) % 100
                test = actual
            else:
                actual = test
        
        if actual == 0:
            zeros += 1
            
                
print("password:", zeros)