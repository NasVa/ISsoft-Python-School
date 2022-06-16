input_string = ""
input_symbol = ""
while input_string == "":
    input_string = input("Enter string: ")
while input_symbol == "":
    input_symbol = input("Enter symbol: ")
for i in input_string:
    if i == input_symbol:
        print("Entered string contains entered symbol")
        break
else:
    print("Entered string doesn't contain the entered symbol")
    
