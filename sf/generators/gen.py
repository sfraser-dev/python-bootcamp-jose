def cube_them_normally(val_in):
    res = []
    for x in range(0, val_in):
        res.append(x**3)
    return res

def cube_them_via_generator(val_in):
    for x in range(0, val_in):
       yield x**3

# generate fibs ineffciently
def fib_seq_normal(val_in):
    a = 1
    b = 1
    li = []
    for i in range(0, val_in):
        li.append(a)
        a,b = (b,a+b)
    return li

# generate fibs efficiency
def fib_seq_efficient(val_in):
    a = 1
    b = 1
    for i in range(0, val_in):
        yield a
        a,b = (b,a+b)

def simple_gen():
    for x in range(0,3):
        yield x

# not memory efficient
li = cube_them_normally(10)
print(li)

# much more memory efficient
# only need one value at a time, don't need heaps of numbers stored in memory
for x in cube_them_via_generator(10):
    print(x)

for x in fib_seq_normal(100):
    print(x)

for x in fib_seq_efficient(100):
    print(x)

# next keyword (we won't be using next hardly at all, it's a behind the scences part of generators/yield)
# create a generator object and call next upon it to get the next yield
generator_object = simple_gen()
print(next(generator_object))
print(next(generator_object))
print(next(generator_object))

# iter keyword (we won't be using iter hardly at all, it's a behind the scences part of generators/yield)
# iter keyword
s = 'hello'
# cannot do "next(s)"", get error "str object is not an iterator"
#next(s)
s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))

