def foo():
    raise RuntimeError
foo()

try:
    foo()
except RuntimeError:
    print("Caught RuntimeError")
except MemoryError:
    print("Caught MemoryError")
except AssertionError:
    print("Caught AssertionError")