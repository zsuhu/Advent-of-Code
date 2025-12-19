with open("day2_testcase.txt") as f:
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
        for i in range(2, len(num)):

            if len(num) % i == 0:
                invalid = True
                sep = len(num) // i
                for j in range(0,len(num)-sep,sep):
                    if num[j:sep] != num[j+sep:sep+sep]:
                        invalid = False
                        break
                        
                if invalid:
                    total += int(num)
            
print(total)