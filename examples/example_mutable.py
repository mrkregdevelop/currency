def foo(a: int, b=None):
    if b is None:
        b = []
    b.append(a)
    print(b)


foo(1)
foo(2)
foo(3, list())
