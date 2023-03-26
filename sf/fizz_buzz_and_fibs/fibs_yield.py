# generate fibs efficiency (generator)
def fib_seq_efficient(val_in):
    a = 1
    b = 1
    for i in range(0, val_in):
        yield a
        a,b = (b,a+b)

for x in fib_seq_efficient(30):
    print(x)