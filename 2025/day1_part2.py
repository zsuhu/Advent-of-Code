actual = 50
zeros = 0

with open("day1_input.txt") as f:
    for line in f:
        direction = line[:1]
        distance = int(line.strip()[1:len(line)])
        
        if direction == 'R':
            if actual + distance > 99:
                zeros += (actual + distance) // 100
                actual = (actual + distance) % 100
            else:
                actual += distance 
                
        elif direction == 'L':
            if actual == 0:
                if abs((actual - distance) // 100) > 1:
                    zeros += abs((actual - distance)) // 100
                    actual = (actual - distance) % 100 
                    continue 
                actual = (actual - distance) % 100
                if actual == 0:
                    zeros += 1
            elif actual - distance < 0:
                zeros += abs((actual - distance) // 100)
                actual = (actual - distance) % 100
                if actual == 0:
                    zeros += 1
            elif actual - distance == 0:
                zeros += 1
                actual -= distance
            else:
                actual -= distance


        print(actual, zeros)
                
print("password:", zeros)