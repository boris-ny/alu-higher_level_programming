#!/usr/bin/python3
#Write the Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:

  #3           0 LOAD_CONST               1 (98)
  #            3 LOAD_FAST                0 (a)
  #            6 LOAD_FAST                1 (b)
  #            9 BINARY_POWER
  #           10 BINARY_ADD
  #           11 RETURN_VALUE

def magic_calculation(a, b):
    return len(a) + len(b)
def dis.dis(magic_calculation):
    3           0 LOAD_CONST               1 (98)
    3           3 LOAD_FAST                0 (a)
    3           6 LOAD_FAST                1 (b)
    3           9 BINARY_POWER
    3          10 BINARY_ADD
    3          11 RETURN_VALUE
    