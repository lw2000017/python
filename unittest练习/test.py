# from cccc import Count

# class TestCount():
#     def test_add(self):
#         try:
#             j = Count(2,3)
#             add = j.add()
#             assert (add == 5),"Integer addition result error!"
#         except AssertionError as msg:
#             print(msg)
#         else:
#             print("Test Pass!")
#
# mytest=TestCount()
# mytest.test_add()

print('for x in iter([1, 2, 3, 4, 5]):')
for x in iter([1, 2, 3, 4, 5]):
    print(x)

print('for x in [1, 2, 3, 4, 5]:')
for x in [1, 2, 3, 4, 5]:
    print(x)


print('next():')
it = iter([1, 2, 3, 4, 5])
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))