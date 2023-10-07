"""
What will be the output? Why?

ANSWER
(base) SnoopMac:code-problems topher$ python simple_function_return.py 
Traceback (most recent call last):
  File "simple_function_return.py", line 10, in <module>
    (a, b) = apple_varieties()
ValueError: too many values to unpack
"""


def apple_varieties():
    return 'fuji', 'braeburn', 'gala'


(a, b, c,) = apple_varieties()
print(a, b)
