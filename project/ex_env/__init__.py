

class Package():

    def __init__(self, name, fields={}, commands={}):
        self.fields = fields
        self.commands = commands
        self.name = name

    def run(self):
        while True:
            user_in = input(self.name + ' >> ')
            if user_in == '':
                continue
            user_in = user_in.split(' ')
            command = user_in[0]
            args = user_in[1:]
            if '.' in command:
                print('TODO handle sub-package commands')
            elif command == 'help':
                self.commands[args[0]].help(args[1:], self.fields)
            elif not self.contains_command(command):
                print('command "' + command + "' not recognized")
            else:
                exe_cmd = self.commands[command]
                exe_cmd.execute(args, self.fields)

    def contains_command(self, command):
        return command in self.commands

    def execute(self, args, fields):
        self.run()

    def add_command(self, command, name):
        if name in self.commands:
            print("that command alread exists in package", self.name)
        else:
            self.commands[name] = command

    def is_package(self):
        return True


def default_help(args, fields):
    print("no help function is defined for this function")


class Command():

    def __init__(self, func, help=default_help):
        self.execute = func
        self.help = help

    def is_package(self):
        return False
