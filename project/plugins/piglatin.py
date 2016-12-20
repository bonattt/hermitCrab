from ex_env import Package

def import_to(env):
    env.add_command(PigLatinCommand(), "pig")


class PigLatinCommand():

    def __init__(self):
        pass

    def execute(self, args, fields):
        msg = ""
        for word in args:
            msg += pig_latinize(word)
            msg += ' '
        print(msg)


def pig_latinize(word):
    first = word[0]
    word = word[1:]
    word = word + first + 'ay'
    return word