an_value = 0
sn_value = 0
for i in range(1,10):
    an_value = 1/(i**2)
    sn_value += an_value 
    print("n=",i, " an=",an_value, " Sn=", sn_value)
