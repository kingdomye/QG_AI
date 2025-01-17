def int_number_example():
    # int类型数据范围
    number1 = 78
    print("Small integer output", number1)
    number2 = 66666666666666666666666666666
    print("Big integer output", number2)

    # int类型运算
    print("addition", number1 + number2)
    print("subtraction", number1 - number2)
    print("multiplication", number1 * number2)
    print("division", number2 / number1)
    print("divisible", number2 // number1)
    print("remainder", number2 % number1)
    # print("exponent", number1 ** number2) 太慢了注释掉😅

    # 2、8、16进制
    bin_number = 0b1110
    oct_number = 0o75
    hex_number = 0xF5
    print("Binary output", bin_number)
    print("Octal output", oct_number)
    print("Hex output", hex_number)

    return


if __name__ == '__main__':
    int_number_example()
