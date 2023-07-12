size = 10
def print_rdn_number():
    number =random.randint(0,9)
    return number
    
sum =0
for i in range(0,size):
    for j in range(0,size):
        if j ==0 or j==size-1:
            number = print_rdn_number()
            sum+=number
            print(number, end="")
        elif j == size -i-1:
            number=print_rdn_number()
            sum+=number
            print(number, end="")
        elif i ==j:
            number =print_rdn_number()
            sum+=number
            print(number, end="")
        elif i ==0 or i ==size-1:
            number= print_rdn_number()
            sum+=number
            print(number, end="")
        else:
            print("_", end="")
        
    print("")
