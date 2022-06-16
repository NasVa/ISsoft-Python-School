def decimal_to_another(num, system):

    def dec_int_to_another(num, system):
        result = ""
        while num:
            result += (chr(ord('A') + (num % system - 10))) if num % system > 9 else str(num % system)
            num //= system
        return "".join(reversed(result))

    result = dec_int_to_another(int(str(num).split(".")[0]), system) + "."
    float_res = num - int(num)
    while float_res:
        float_res *= system
        result += str(chr(ord('A') + int(float_res) - 10) if int(float_res) >= 10 else int(float_res))
        float_res -= int(float_res)
    return result


def another_to_decimal(num, system):

    def another_int_to_dec(num, system):
        result = 0
        for i in range(len(num)):
            result += int(((10 + (ord(num[i]) - ord('A'))) if ord(num[i]) >= ord('A') else num[i])) * system ** (len(num) - i - 1)
        return result

    result = float(another_int_to_dec(num.split(".")[0], system))
    float_res = num.split(".")[1]
    for i in range(len(float_res)):
        result += int((10 + (ord(float_res[i]) - ord('A'))) if ord(float_res[i]) >= ord('A') else float_res[i]) * system ** -(i + 1)
    return result

def translate(original_num, original_system, result_system):
    if result_system == 10:
        return another_to_decimal(original_num, original_system)
    else:
        decimal_res = another_to_decimal(original_num, original_system)
        return(decimal_to_another(decimal_res, result_system))

orig_num = input("Enter the original value: ")
orig_sys = input("Enter the original system: ")
res_sys = input("Enter the result system: ")
print(translate(orig_num, int(orig_sys), int(res_sys)))
#print(another_int_to_dec('100101', 2))