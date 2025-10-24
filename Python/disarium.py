def is_disarium(number):
    
    original_number = number
    sum_of_powers = 0
    
   
    num_str = str(number)
    length = len(num_str)
    
    
    for i in range(length):
        digit = int(num_str[i])
        sum_of_powers += digit ** (i + 1)  
        
    
    return sum_of_powers == original_number


num = int(input("Enter a number: "))


if is_disarium(num):
    print(f"{num} is a Disarium number.")
else:
    print(f"{num} is not a Disarium number.")