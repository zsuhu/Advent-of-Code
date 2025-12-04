actual = 50
zeros = 0

with open("day1_input.txt") as f:
    for line in f:
        direction = line[:1]
        distance = int(line.strip()[1:len(line)])
        
        if direction == 'R':
            if actual + distance > 99:
                actual = (actual + distance) % 100
            else:
                actual += distance
                
        elif direction == 'L':
            if actual - distance < 0:
                actual = (actual - distance) % 100
            else:
                actual -= distance
        
        if actual == 0:
            zeros += 1
            
                
print("password:", zeros)