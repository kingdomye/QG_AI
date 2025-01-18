def conditional_control():
    number1, number2 = map(int, input().split())
    if number1 > number2:
        print("number1 is greater than number2")
    else:
        print("number2 is greater than number1")

    number3 = int(input())
    if number3 < 0:
        print("number3 < 0")
    elif number3 == 0:
        print("number3 = 0")
    else:
        print("number3 > 0")


def loop_control():
    sum, i = 0, 0
    while i < 10:
        sum += i
        i += 1

    for i in range(10):
        print(i)


if __name__ == '__main__':
    conditional_control()
