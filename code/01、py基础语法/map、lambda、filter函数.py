def map_example():
    def func(n):
        return n * 2

    my_list = map(func, range(10))
    print(list(my_list))


def lambda_example():
    func1 = lambda: "welcome to QG!"
    print(func1())

    func2 = lambda n: n * 2
    print(func2(5))

    func3 = lambda a, b: a * b
    print(func3(5, 7))


def filter_example():
    def is_even(n):
        return n % 2 == 0
    my_list = filter(is_even, range(1, 10))
    print(list(my_list))


if __name__ == '__main__':
    filter_example()
