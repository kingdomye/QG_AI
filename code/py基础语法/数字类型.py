def int_number_example():
    # int类型数据范围
    int_number1 = 78
    int_number2 = 66666666666666666666666666666
    print("Small integer output", int_number1)
    print("Big integer output", int_number2)

    # int类型运算
    print("addition", int_number1 + int_number2)
    print("subtraction", int_number1 - int_number2)
    print("multiplication", int_number1 * int_number2)
    print("division", int_number2 / int_number1)
    print("divisible", int_number2 // int_number1)
    print("remainder", int_number2 % int_number1)
    # print("exponent", int_number1 ** int_number2) 太慢了注释掉😅

    # 2、8、16进制
    bin_number = 0b1110
    oct_number = 0o75
    hex_number = 0xF5
    print("Binary output", bin_number)
    print("Octal output", oct_number)
    print("Hex output", hex_number)


def float_number_example():
    float_number1 = 1.18
    float_number2 = 13.2981798639218

    # float类型运算
    print("addition", float_number1 + float_number2)
    print("subtraction", float_number1 - float_number2)
    print("multiplication", float_number1 * float_number2)
    print("division", float_number2 / float_number1)
    print("divisible", float_number2 // float_number1)
    print("remainder", float_number2 % float_number1)
    print("exponent", float_number2 ** float_number1)


def bool_example():
    bool_true = True
    bool_false = False

    print("【bool output】", bool_true, bool_false)
    print("and", bool_true & bool_false)
    print("or", bool_true | bool_false)
    print("xor", bool_true ^ bool_false)
    print("not", not bool_true)


if __name__ == '__main__':
    bool_example()
