#!/usr/bin/python3


def static_var(varname, value):
    def decorator(func):
        setattr(func, varname, value)
        return func
    return decorator


@static_var("x", 0)
def foo():
    foo.x += 1
    print("%d" % foo.x)


def test41():
    foo()
    foo()
    foo()


test41()
