from ex_env import Package, Command

def run():
    env = Package("Hermit-Crab")
    env.add_command(Command(echo), "echo")
    env.add_command(Command(q), "q")
    env.add_command(Command(q), "quit")
    env.add_command(Command(q), "exit")
    env.run()

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
    try:
        accumulator = 0
        for numb in args:
            accumulator += int(numb)
    except Exception as a:
        print(a)


if __name__ == "__main__":
    run()