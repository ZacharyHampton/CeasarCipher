import requests

# app -> +1 zoo | app -> +12 odd

specialchar = " !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ") # Alphabet that gets split into each char and put into list


def shiftCS(encodedMessage, shiftValue):  # Negative shift value decodes and positive shift value encodes

	message = ""  # Decode holder
	for x in encodedMessage:  # for each char
		if x not in specialchar: # if not special char
				message += letters[(letters.index(x.upper()) + shiftValue) % 26]  # shift 
		else:
			message += x  # add special char to list
			
	return message

def shiftWKey(encodedMessage, password, choice):  # Negative shift value decodes and positive shift value encodes
	password = bytes(password, 'utf-8')

	password = [y for y in password]
	message = ""  # Decode holder
	i = 0
	for x in encodedMessage:  # for each char
		if x not in specialchar: # if not special char
			if choice == "encode":
				message += letters[(letters.index(x.upper()) + (password[i % len(password)] % len(password))) % 26]  # shift
			elif choice == "decode":
				message += letters[(letters.index(x.upper()) - (password[i % len(password)] % len(password))) % 26]  # shift
			i += 1
		else:
			message += x  # add special char to list
			
	return message

#print(shiftCS("Pm ol ohk hufaopun jvumpkluaphs av zhf, ol dyval pa pu jpwoly, aoha pz, if zv johunpun aol vykly vm aol slaalyz vm aol hswohila, aoha uva h dvyk jvbsk il thkl vba.", -7))

#print(shiftCS("IF HE HAD ANYTHING CONFIDENTIAL TO SAY, HE WROTE IT IN CIPHER, THAT IS, BY SO CHANGING THE ORDER OF THE LETTERS OF THE ALPHABET, THAT NOT A WORD COULD BE MADE OUT.", 7))


def isWord(word):
	response = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}')
	if "No Definitions Found" in response.text:
		return False
	else:
		return True

def bruteforceCipher(encodedMessage):
	shift = 0

	testableword = ""
	encodedMessageSplit = encodedMessage.split(" ")

	for g in encodedMessageSplit:
		if len(g) >= 2 and g not in specialchar:
			testableword = g
			break

	print("Bruting...")
	for x in range(26):
		curwordSplit = list(testableword.upper())

		curword = ""
		for p in range(len(curwordSplit)):
			if curwordSplit[p] not in specialchar:
				curword += letters[letters.index(curwordSplit[p]) - shift]

		if isWord(curword):
			print(f"The shift is -{shift}.")
			return shiftCS(encodedMessage, -shift)
			
		shift += 1

#print(bruteforceCipher("Zrgubq va juvpu rnpu yrggre va gur cynvagrkg vf ercynprq ol n yrggre fbzr svkrq ahzore bs cbfvgvbaf qbja gur nycunorg. Gur zrgubq vf anzrq nsgre Whyvhf Pnrfne Pelcgvv Jro ncc bssrevat zbqhyne pbairefvba, rapbqvat naq rapelcgvba bayvar. Genafyngvbaf ner qbar va gur oebjfre jvgubhg nal freire vagrenpgvba. Cbjrerq ol Jvrex Fghqvb. Pbqr yvprafrq ZVG."))
#print(bruteforceCipher('Method in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. The method is named after Julius Caesar Cryptii Web app offering modular conversion, encoding and encryption online. Translations are done in the browser without any server interaction. Powered by Wierk Studio. Code licensed MIT.'))
#print(bruteforceCipher('hufaopun jvumpkluaphs'))

#encMessage = input("Encrypted Message:\n")
#print(bruteforceCipher(encMessage))

msg = shiftWKey("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "Password123r4tgfregdfredge", "encode")
print(msg)
print(shiftWKey(msg, "Password123r4tgfregdfredge", "decode"))

print(bruteforceCipher('hufaopun jvumpkluaphs'))

