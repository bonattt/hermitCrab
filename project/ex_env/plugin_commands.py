import os
import shutil
import importlib
import ast
import sys


class InstallCommand():

    required_functions = {'import_to': 1, 'remove_from': 1}

    def execute(self, args, fields):
        # todo implement package import
        if len(args) != 1:
            print("install command expects exactly 1 argument")
            return

        filepath = args[0]
        if not filepath.endswith('.py'):
            print("that is not a python file!!")
            return

        abspath = os.path.abspath(filepath)
        filename = abspath.split('\\')[-1]
        copy_to_path = fields["_dir_"] + 'plugins/' + filename
        if os.path.exists(copy_to_path):
            print("the file '" + filename + "' already exists, import aborted!")
            return

        if not module_complies_to_interface(abspath):
            print("install aborted")
            return

        if os.path.isdir(abspath):
            print('cannot import a directory!')
        elif filename.endswith('.py'):
            self.install_single_file(abspath, copy_to_path, filename, fields)
        else:
            print("aborting unknown install ...")

    def install_single_file(self, abspath, copy_to_path, filename, fields):
        # print('copy:', copy_to_path)
        # print('abs: ', abspath)
        shutil.copyfile(abspath, copy_to_path)
        man_file = open(fields['_dir_'] + 'manifest', 'a')
        man_file.write(filename)
        man_file.close()
        print('successfully installed"' + filename + '"')
        fields['_env_'].import_new_plugin(filename)

    def help(self, args, fields):
        print("use import to easily import new python modules")
        print("import <filepath>")
        print("this function will copy the file you wish to install to ")


def module_complies_to_interface(file_path):
    complies = True
    file_name = file_path.split('\\')[-1]
    file = open(file_path, 'rt')
    tree = ast.parse(file.read(), filename=file_name)

    impl_func_names = top_level_function_names(tree.body)
    for func in InstallCommand.required_functions:
        if not func in impl_func_names:
            complies = False
            print('ERROR: required function "' + func + '" not implemented in plugin')

    impl_funcs = top_level_functions(tree.body)
    for func in impl_funcs:
        if func.name in InstallCommand.required_functions:
            argsExpected = InstallCommand.required_functions[func.name]
            if func.args != argsExpected:
                # complies = False
                print('WARNING: function "' + func.name + '" has ' + str(func.args) +
                      ' args and should have ' + str(argsExpected))
            else:
                print('function "' + func.name + '" complies with expected standards')
        else:
            print('function "' + func.name + '" not a required function')

    file.close()
    return complies


def top_level_function_names(body):
    ls = []
    for obj in body:
        if isinstance(obj, ast.FunctionDef):
            ls.append(obj.name)
    return ls


def top_level_functions(body):
    return (f for f in body if isinstance(f, ast.FunctionDef))


class UninstallCommand():

    def execute(self, args, fields):
        if (len(args) != 1):
            print("uninstall command expects exactly 1 argument")
            return

        plugin_name = args[0]
        plugin_filename = plugin_name + '.py'
        man_file = open(fields['_dir_'] + 'manifest', 'r')
        file_text = man_file.read().split('\n')
        man_file.close()
        if not (plugin_filename) in file_text:
            print("there is no plugin called '" + plugin_name + "'")
            return
        file_text.remove(plugin_filename)
        deleted_module = importlib.import_module('plugins.' + plugin_name)
        deleted_module.remove_from(fields["_env_"])
        man_file = open(fields['_dir_'] + 'manifest', 'w')
        for line in file_text:
            man_file.write(line)
        man_file.close()
        os.remove(fields['_dir_'] + 'plugins/' + plugin_filename)
        print('successfully removed ' + plugin_name)

    def help(self, args, fields):
        print("this command uninstalls the given plugin.")
        print("uninstall <plugin name>")