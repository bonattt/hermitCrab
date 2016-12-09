

class ExecutionEnv():

    def __inti__(self, fields={}, commands={}):
        self.fields = fields
        self.commands = commands

    def run(self, path_name):
        while True:
            user_in = input(path_name + ' >> ')
            if user_in == '':
                continue

            user_in = user_in.split(' ')
            command = user_in[0]
