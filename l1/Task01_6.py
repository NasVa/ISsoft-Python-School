a = 0
b = 0
c = 0
    
def enter_value(value):
    num = 0
    while num == 0:
        str_value = input(f"Enter the value of {value}: ")
        if str_value.isdigit() and int(str_value) > 0:
            return int(str_value)

a = enter_value("A")
b = enter_value("B")
c = enter_value("C")
print("Number of squares: " + str((a//c)*(b//c)))
        
