class A():
    pass


class B(A):
    pass


class C(B):
    pass


class D(C):
    pass


result = []
if issubclass(D, A):
    result.append('A')
if issubclass(D, B):
    result.append('B')
if issubclass(D, C):
    result.append('C')

print(" ".join(sorted(result)))
