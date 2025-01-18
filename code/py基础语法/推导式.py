print("列表推导式", [x for x in range(10)])
print("字典推导式", {x: x for x in (1, 2, 3)})
print("集合推导式", {x for x in 'abracadabra' if x not in 'abc'})
print("元组推导式", tuple((x for x in range(1, 10))))
