def is_happy_number(n):

    num_set = set()
    
    while n not in num_set:
        num_set.add(n)
        if n == 1:
            return True
        squared_sum = 0   
        while n > 0:
            digit = n % 10
            squared_sum += digit ** 2
            n = int(n/10)
        n = squared_sum
    return False

print(is_happy_number(7))