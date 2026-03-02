# sum of square of numbers
def squre_number(num):
    total = 0 
    while num > 0:
        digit = num % 10   #9   1
        total = total + (digit * digit)  #81  82
        num = num // 10  # 1  
    return total    #82
print(squre_number(19))
    