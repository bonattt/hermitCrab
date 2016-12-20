
"""
from math import sin
from math import cos
from math import tan
from math import asin
from math import acos
from math import atan
from math import pow
"""
import math


class ArithmeticCommand():

    OPERATIONS = [
        '+', '-', '*', '/',
    ]

    def __init__(self):
        self.math_stack = []

    def execute(self, args, fields):
        for item in args:
            if item == '+':
                self.math_stack[-1] = '+'

            elif item == '-':
                self.math_stack[-1] = '-'

            elif item == '/':
                self.math_stack[-1] = '/'

            elif item == '*':
                self.math_stack[-1] = '*'

            elif item == '(':
                print("TODO - impliment parentheses")

            elif item == ')':
                print("TODO - impliment parentheses")

            elif item == '**':
                print("TODO - impliment pow")

            elif item in fields:
                self.math_stack[-1] = fields[item]

            else:
                self.stack_number(item)
        self.evaluate()

    def stack_number(self, numb):
         try:
            if '.' in numb:
                numb = float(numb)
            else:
                numb = int(numb)
            self.math_stack.append(numb)

         except ValueError as e:
            print('"' + str(numb) + '" is not a valid arithmetic symbol')

    def evaluate(self):
        pass

    def evaluate_mult(self):
        arg1 = self.math_stack.pop()
        arg2 = self.math_stack.pop()
        self.math_stack.append(arg1 * arg2)

    def help(self, args, fields):
        print("TODO - impliment math help")
