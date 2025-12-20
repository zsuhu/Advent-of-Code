with open("day2_input.txt") as f:
    string = f.read()
    ranges = string.strip().split(',')
    #print(ranges)
      
total = 0
for ids in ranges:
    edges = ids.split('-')
    start, end = int(edges[0]), int(edges[1])
    nums = []
    for i in range(start, end+1):
        nums.append(str(i))
    
    for num in nums:
        for i in range(2, len(num)+1):

            if len(num) % i == 0:
                invalid = True
                sep = len(num) // i
                for j in range(0,len(num)-sep,sep):
                    if num[j:j+sep] != num[j+sep:j+sep+sep]:
                        invalid = False
                        break
                        
                if invalid:
                    #print(nums, num)
                    total += int(num)
                    break
            
print(total)