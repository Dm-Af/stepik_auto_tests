# print('Hello! It is main.py!')
# import lesson_2_4_7.py
# print('End of Main.py file!')

import sys
from contextlib import contextmanager

@contextmanager
def reversed_print():
    def reserved_write(text):
        original_write(text[::-1])
    original_write = sys.stdout.write
    sys.stdout.write = reserved_write
    yield
    sys.stdout.write = original_write

with reversed_print():
    print('Вывод внутри блока with')

print('Вывод вне блока with')
