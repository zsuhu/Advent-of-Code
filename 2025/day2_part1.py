with open("day2_input.txt") as f:
    string = f.read()
    ranges = string.strip().split(',')
      
total = 0
for ids in ranges:
    edges = ids.split('-')
    start, end = int(edges[0]), int(edges[1])
    nums = []
    for i in range(start, end+1):
        nums.append(str(i))
    
    for num in nums:
        if len(num) % 2 == 1:
            continue
        
        mid = len(num) // 2    
        if num[:mid] == num[mid:]:
            total += int(num)
            
print(total)