from ex_env import Package, Command
from hc_math import MathPackage
import plugins
# from plugins.piglatin import PigLatinCommand
import json
import importlib
import os # TODO remove this

def run():
    env = Package("Hermit-Crab")

    env.import_plugins("./")

    # pig_latin = importlib.import_module("plugins.piglatin")
    # print(pig_latin)
    # print(pig_latin.pig_latinize("hello"))

    env.add_command(Command(echo), "echo")
    env.add_command(Command(q), "q")
    env.add_command(Command(q), "quit")
    env.add_command(Command(q), "exit")
    env.add_command(Command(plus), "+")
    env.add_command(MathPackage(), "math")

    env.add_field("one", 1)
    env.add_field("two", 2)
    env.add_field("three", 3)
    env.add_field("four", 4)
    env.add_field("five", 5)
    env.add_field("six", 6)

    env.run()


def import_plugins(filepath, env):
    with open(filepath) as data_file:
        data = json.load(data_file)
    print("DEBUG: " + str(data))
    print(type(data))
    for plugin in data:
        plugin_data = data[plugin]
        for plugin_item in plugin_data:
            if plugin_item.endswith(".py"):
                handle_plugin_file(plugin_item, plugin_data, env)
            else:
                handle_plugin_field(plugin_item, plugin_data, env)


def handle_plugin_file(plugin_name, plugin_data, env):
    plugin_file = plugin_data[plugin_name]
    for command_name in plugin_file:
        command_class = plugin_file[command_name]
        importCommand(command_class, plugin_name, command_name, env)


def handle_plugin_field(field_name, plugin_data, env):
    field_val = plugin_data[field_name]
    print("adding global field:", field_name, "=", field_val)
    env.add_field(field_name, field_val)


def importCommand(command_class, plugin_name, command_name, env):
    print('adding command "' + command_class + '"')
    # import_statement = 'from plugins.' + plugin_name[:-3] + ' import ' + command_class
    add_command_statement = 'env.add_command('
    add_command_statement += 'plugins.' + plugin_name[:-3] + '.' + command_class + '(), "' + command_name + '")'
    print('eval(' + add_command_statement + ')')
    eval(add_command_statement)


def echo(args, fields):
    for item in args:
        print(item)

def q(args, fields):
    if not '--yes' in args:
        user_in = input("are you sure you would like to quit? (yes/no) ")
        if not user_in.startswith('y'):
            return
    exit(0);

def plus(args, fields):
    accumulator = 0
    for numb in args:
        try:
            numb = int(numb)
            accumulator += numb
        except ValueError:
            try:
                numb = float(numb)
                accumulator += numb
            except ValueError:
                print('invlaid arg "' + numb +'"')
    print(accumulator)


if __name__ == "__main__":
    # print('locpath: ./manifest')
    # print('abspath:', os.path.abspath("./manifest"))
    run()