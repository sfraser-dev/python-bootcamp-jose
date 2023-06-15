def func():
    print("func() in one.py") 

def function1():
    pass

def function2():
    pass

# this is used like main() in C for code organisation
# rather than using indents for where to enter program, creat a quasi main()
if __name__ == "__main__":
    print("top level in one.py")
    function1()
    function2()
    print("one.py is being run directly")
else: # not normally this else block, just for info here
    print("one.py has been imported")
