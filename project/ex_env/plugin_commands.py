import os
import shutil
import importlib


class InstallCommand():

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

        if os.path.isdir(abspath):
            print('cannot import a directory!')
        elif filename.endswith('.py'):
            self.import_single_file(abspath, copy_to_path, filename, fields)

    def import_single_file(self, abspath, copy_to_path, filename, fields):
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