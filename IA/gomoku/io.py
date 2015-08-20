# caian 20/08/2015

"""
Input and console functions
"""
console = "> "

def ask(message=None):
	if message != None:
		s = "%s\n%s" % (message, console)
	else:
		s = console
	return raw_input(s)

def ask_num(message=None):
    return int(ask(message))

