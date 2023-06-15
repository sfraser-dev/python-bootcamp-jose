# We won't be expected to create decorators like this as part of our code
# Rather, we will be using decorators within web-frameworks or libraries 
# so we can inject our own additional functionality / information
def i_decorate(plea):

    def wrap_func():
        print('new code top..')
        plea()
        print('new code bottom..')
    
    # return the wrapping function in the decorator
    return wrap_func

if __name__ == '__main__':
    
    def plea():
        print('I want to be decorated')

    @i_decorate
    def plea2():
        print('I want to be decorated')

    print('---long way of manually "decorating" a function')
    decorated = i_decorate(plea)
    decorated()

    print('---python decorator way')
    plea2()

