import os
import shutil


class ImportCommand():

    def execute(self, args, fields):
        # todo implement package import
        filepath = args[0]
        if not filepath.endswith('.py'):
            print("that is not a python file!!")
            return

        abspath = os.path.abspath(filepath)
        filename = abspath.split('\\')[-1]
        copy_to_path = './plugins/' + filename
        if os.path.exists(copy_to_path):
            print("the file '" + filename + "' already exists, import aborted!")
            return

        if os.path.isdir(abspath):
            print('cannot import a directory!')
        elif filename.endswith('.py'):
            self.import_single_file(abspath, copy_to_path, filename, fields["_env_"])

    def import_single_file(self, abspath, copy_to_path, filename, env):
        # print('copy:', copy_to_path)
        # print('abs: ', abspath)
        shutil.copyfile(abspath, copy_to_path)
        man_file = open('./manifest', 'a')
        man_file.write(filename)
        man_file.close()
        print('successfully installed"' + filename + '"')
        env.import_new_plugin(filename)


    def help(self, args, fields):
        print("use import to easily import new python modules")
        print("import <filepath>")
        print("this function will copy the file you wish to install to ")