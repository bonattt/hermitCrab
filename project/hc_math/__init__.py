from ex_env import Package
import hc_math.math_commands

class MathPackage(Package):

    def __init__(self):
        self.name = "math"

        self.commands = {"=": math_commands.ArithmeticCommand()}

        self.fields = {
            "pi": 3.14159,
            "e": 2.718281828
        }



