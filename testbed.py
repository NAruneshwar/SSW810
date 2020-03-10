def foo(x, use_max = True, *values):
    return x + (min(values) if use_max else max(values))

print (foo(1,2,3,4))