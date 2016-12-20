from random import randint


def import_to(env):
	env.add_command(RngenCommand(), 'rn')
	env.add_command(RngenCommand(), 'rngen')
	
	
def remove_from(env):
	env.remove_command('rn')
	env.remove_command('rngen')	
	
	
class RngenCommand():

	def execute(args, fields):
		if len(args) == 0:
			run()
		else:
			for num in args:
				getRN(num)
				
	def help(args, fields):
		print("rngen produces a random number between 1 and <num> inclusive")
		print("rngen <num> ...")


def run():
	print('Welcom to RNgen.\nType a number to get a random integer between 1 and that number.\npress q to exit')
	while True:
		print()
		numb = input('#> ')
		if numb.startswith('q'):
			break
		getRN(numb)
			
def getRN(numb):
		try:
			numbInt = int(numb)
			print(randint(1,numbInt))
		except:
			print('not a number')
			
	
if __name__ == "__main__":
	run()