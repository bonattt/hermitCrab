import importlib
from ex_env.plugin_commands import InstallCommand, UninstallCommand


class Package():

    restricted_names = ["install"]
    restricted_fields = ["_env_", "_dir_"]

    def __init__(self, name, root_dir='./', fields={}, commands={}):
        self.fields = fields
        self.commands = commands
        self.name = name

        self.fields["_env_"] = self
        self.fields["_dir_"] = root_dir

        self.commands["install"] = InstallCommand()
        self.commands["uninstall"] = UninstallCommand()

    def import_plugins(self, rootdir):
        file = open(rootdir + 'manifest')
        plugins = file.read().split('\n')
        for plugin_file in plugins:
            if plugin_file == '':
                break
            self.import_new_plugin(plugin_file)

        file.close()
        pass

    def import_new_plugin(self, plugin_file):
        try:
            if not plugin_file.endswith('.py'):
                print("ERROR: tried to import non-python file '" + plugin_file + "'!!")
                return
            plugin_module = plugin_file[:-3] # remove .py
            mod = importlib.import_module('plugins.' + plugin_module)
            mod.import_to(self)
            print("successfully imported module '" + plugin_module + "'")
        except Exception as e:
            print("an error occurred while importing:")
            print(e)
        except AttributeError as e:
            print("an error occurred while importing:")
            print(e)
            print("make sure the function import_to(environment) is defined in the module you are trying to import.")


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
                if len(args) < 1:
                    print('try: help <command>')
                self.commands[args[0]].help(args[1:], self.fields)

            elif command == 'field' or command == 'f':
                if (len(args) == 0):
                    for field in self.fields:
                        print(field + ': ' + str(self.fields[field]))

                elif len(args) != 1:
                    print('type field then a package\'s field to see the value of that field')
                elif not args[0] in self.fields:
                    print('"' + args[0] + '" is not a field in the package "' + self.name + '"')
                else:
                    print(self.fields[args[0]])


            elif not self.contains_command(command):
                print('command "' + command + '" not recognized')
            else:
                exe_cmd = self.commands[command]
                exe_cmd.execute(args, self.fields)

    def contains_command(self, command):
        return command in self.commands

    def execute(self, args, fields):
        self.run()

    def add_command(self, command, name):
        if name in self.restricted_names:
            raise Exception("cannot overwrite the command '" + name + "' with a user command.")
        if name in self.commands:
            print("that command alread exists in package", self.name)
        else:
            self.commands[name] = command

    def remove_command(self, name):
        if name in self.commands:
            self.commands.pop(name)

    def add_field(self, name, value):
        if name in self.restricted_fields:
            raise Exception("cannot assign a value to a restricted field + '" + name + "'")
        self.fields[name] = value

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
