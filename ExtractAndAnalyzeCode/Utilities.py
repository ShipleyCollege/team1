###
#  FUNCTION : get string between quotes
###
def getQuotedString(string):
	return string.split('"')[1]
	

###
#  FUNCTION : add a space before any capital letter
###	
def addSpaces(text):
	new_text = ''
	is_first_letter = True

	for letter in text:
		if (not is_first_letter) and letter.isupper():
			new_text += ' ' + letter
		else:
			new_text += letter
		is_first_letter = False

	return " ".join(new_text.split())  # remove duplicate spaces

	
	
#print(addSpaces("WordOneAndTwo"))

	