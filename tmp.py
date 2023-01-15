class A:
    pass
class B(A):
    pass
class C(B):
    pass

import inspect
c = C()
print(c)
print(c.__class__.__mro__)
print(inspect.getclasstree(inspect.getmro(c.__class__)))
