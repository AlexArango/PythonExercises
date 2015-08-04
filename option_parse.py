from optparse import OptionParser


def main():
	parser = OptionParser()
	
	parser.add_option("-f", "--file_name", help = "what's the file name of the feed")
	
	parser.add_option("-n", "--your_name", help = "What's your name?")
	
	options, remainder = parser.parse_args()
	
	file_name = options.file_name
	your_name = options.your_name
	
	
	if file_name:
		open_file(file_name)
	else:
		"The file name was not specified, please provide file name"
		
	print "User said to open file: ", file_name
	print "You said your name was: ", your_name




if __name__ == '__main__':
	main()
	
	
