import json
from sklearn.neural_network import MLPClassifier

morse = {'.-': "A",     '-...': "B",   '-.-.': "C", 
         '-..': "D",    '.': "E",      '..-.': "F",
         '--.': "G",    '....': "H",   '..': "I",
         '.---': "J",   '-.-': "K",    '.-..': "L",
         '--': "M",     '-.': "N",     '---': "O",
         '.--.': "P",   '--.-': "Q",   '.-.': "R",
     	 '...': "S",    '-': "T",      '..-': "U",
         '...-': "V",   '.--': "W",    '-..-': "X",
         '-.--': "Y",   '--..': "Z",   '-----': "0",  
         '.----': "1",  '..---': "2",  '...--': "3",  
         '....-': "4",  '.....': "5",  '-....': "6",  
         '--...': "7",  '---..': "8",  '----.': "9", 
         "/": " "}

def translate(message):
	message_list = message.split(" ")
	english = ""
	for letter in message_list:
		english += morse[letter] 
	print(english)
	return None

# def retrieve_image():
# 	f = open("annotation.json", "r")
# 	js = f.read()
# 	image_dict = json.loads(js)
# 	print(image_dict)
# 	f.close()
# 	return None

# if __name__ == "__main__":
# 	retrieve_image()