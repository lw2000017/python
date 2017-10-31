
empty_set=set()#创建一个空的集合
some_set=set([1,2,2,3,4])#给some_set赋予set([1,2,3,4]),集合里不显示重复
filed_set={1,2,2,3,4}
filed_set.add(5)
other_set={3,4,5,6}
print    (filed_set  &other_set)
print (filed_set|other_set)
print  (2 in filed_set)
print  (10 in filed_set)
print ({1,2,3,4}-{2,3,4})



some_var=5

if some_var>10:
    print ("some_var is totally bigger than 10.")
elif some_var<10:
    print ("some_var is smaller than 10.")
else:
    print ("some_var is indeed 10.")


i=1
while i<5:
    print(i)
    i=i+1



def add(x,y):
    print("x is %s and y is %s"%(x,y))
    print("x+y is ",x+y)


add(2,3)
#使用*来接受可变数量的定位参数
def varargs(*args):
    return args

print(varargs(1,2,3,4,5,6,7,8,9,0))

#使用**来接受可变数量的关键字参数
def keyword_args(**kwargs):
    return kwargs


print(keyword_args(big="food",loch="ness"))



def all_the_args(*args,**kwargs):
    print(args)
    print(kwargs)

all_the_args(1,2,3,4,5,6,7,8,a=3,b=4)


def create_adder(x):
    def adder(y):
        return x+y
    return adder
add_10=create_adder(10)
print(add_10(3))

tup=(1,2,3)
print(tup[0])



filled_dict={"one":1,"two":2,"three":3}

filled_dict.setdefault("four",4)
filled_dict.setdefault("five",5)
filled_dict.setdefault("five",6)

print(filled_dict)


print((lambda y: y-5>2)(3))




for i in range(10):
    print (i)
    if i>2:
        print ("dayu2")

a=10
if a<18:
    pass






