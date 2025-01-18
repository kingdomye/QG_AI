def string_example():
    string1 = 'hello QG!'
    string2 = "this is an example"

    print("Access string", string1[2])
    print("String slice", string1[2:5])
    print("String splicing", string1 + string2)
    print("Output strings consecutively", string1 * 2)
    print('Q' in string1)

    formatted_string = "My studio is %s" % "QG"
    print(formatted_string)

    # 字符串内建函数
    print("第一个字符大写", string1.capitalize())
    print("计数", string1.count('l'))
    print("查找索引", string1.find('l'))
    print("替换", string1.replace('l', 'm'))
    # ... ...


def list_example():
    list1 = [1, 2, 3, 4, 5]
    list2 = ['a', 'b', 'c', 'd']

    print("访问列表", list1[2], list2[2: 5], list1[-1])
    print("列表相加", list1 + list2)
    print("列表函数", len(list1), max(list1), min(list1))

    # 列表方法
    list1.append(6)
    print(list1)
    print("计数", list1.count(6))
    print("索引查找", list1.index(6))
    list1.insert(5, 7)
    print("插入", list1)
    list1.pop()
    print("移除最后", list1)
    list1.remove(3)
    print("删除元素", list1)
    list1.reverse()
    print("反转列表", list1)
    list1.sort()
    print("排序", list1)


def dict_example():
    pass


def tuple_example():
    pass


def set_example():
    pass


if __name__ == '__main__':
    list_example()
