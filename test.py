# class parent:
#     def __init__(self, param):
#         self.v1 = param
#
# class child(parent):
#     def __init__(self, param):
#         self.v2 = param
#
# obj = child(11)
# print(obj.v1 + " " + obj.v2)

# confusion = {}
# confusion[(1,2,4)] = 8
# confusion[(4,2,1)] = 10
# confusion[(1,2)] = 12
#
# sum = 0
# for k in confusion:
#     sum += confusion[k]
#
# print(len(confusion) + sum)


# kvps = {'1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5}
# newData = {'1' : 10, '3' : 30}
#
# kvps.update(newData)
#
# x = sum(kvps.values())
# print(x)


# foo = {1 : "1", 2 : "2", 3 : "3"}
# foo = {}
#
# print(len(foo))

# def my_func(x, y, z, a):
#     print(x + y)
#
# nums = [1, 2, 3, 4]
#
# my_func(*nums)

# d = lambda p: p * 2
# t = lambda p: p * 3
# x = 2
# x = d(x)
# x = t(x)
# x = d(x)
# print(x)

# def a(b, c): pass

# x = True
# y = False
# z = False
#
# if not x or y:
#     print(1)
# elif not x or not y and z:
#     print(2)
# elif not x or y or not y and x:
#     print(3)
# else:
#     print(4)

# names = [1, 2, 3, 4]
# names.append([5,6,7,8])
# print(len(names))

# print(4.5 // 2)

# nums = set([1, 1, 2, 3, 3, 3, 4])
# print(len(nums))

# names = ['Rames', 'Rajesh', 'Rojer']

# name = "snow storm"
# name[5] = "X"
# print(name)

# print("\x48\x49!")

# name = "SoftServe IT  Academy"
# print(name.find("IT"))

# my_tuple = (1, 2, 3, 4)
# my_tuple.appe

# foo = {}
# print(type(foo))

# def f(): pass
# print(type(f()))

# print(type(lambda:None))