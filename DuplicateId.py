def duplicate_id(ids):
    if len(ids) == 0:
        return 'Invalid input'
    
    for i in range(len(ids)):
        for j in range(i+1, len(ids)):
            if ids[i] == ids[j]:
                return ids[i]
    else :
         return -1
        

print(duplicate_id([2,3,4,4,4,5,6]))
# Output: 4

