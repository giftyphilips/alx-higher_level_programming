#!/usr/bin/python3
# 101-safe_function.py

def safe_function(fct, *args):
    import sys
    try:
        result = fct(*args)
    except Exception as i:
        sys.stderr.write("Exception: {}\n".format(i))
        result = None

    return (result)
