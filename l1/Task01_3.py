input_value = ""
while input_value == "":
    input_value = input("Enter the value: ")
number_sum = 0
for i in input_value:
    if i.isdigit():
        number_sum += int(i) 
else:
    print("Numbers sum of value: " + str(number_sum))
