def constant(f):
    def fset(self, value):
        raise TypeError
    def fget(self):
        return f()
    return property(fget, fset)

class _Const(object):
    
    @constant
    def intervale():
        return 10
    @constant
    def MacsValues():
        return ['0CF3EE00095A', '0CF3EE00080B', '0CF3EE000598', 'CF3EE000978']
