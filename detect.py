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

train_data_names = []
train_data_labels = []
validation_data_names = []
validation_data_labels = []

def load_json():
   f = open("annotation.json", "r")
   js = f.read()
   image_dict = json.loads(js)
   f.close()
   return image_dict

def create_neural_net(image_dict):
   neural_net = MLPClassifier(hidden_layer_sizes = (100, 50, 25), activation = "relu", solver = "sgd", batch_size = "auto", 
      learning_rate = "constant", learning_rate_init = 0.001, max_iter = 200, shuffle = True)
   training_data = []
   for name in train_data_names:
      training_data.append(image_dict[name])
   neural_net.fit(training_data, train_data_labels)
   return neural_net

def make_predictions(image_dict, neural_net):
   test_data = []
   for name in validation_data_names:
      test_data.append(image_dict[name])
   predictions = neural_net.predict(test_data)
   return predictions

def check_accuracy(predictions):
   s = 0
   for i in range(len(validation_data_labels)):
      if validation_data_labels[i] == predictions[i]:
         s += 1
   accuracy = s / len(validation_data_labels)
   print("Accuracy: " + str(accuracy))
   return accuracy

def translate_predictions(predictions):
   predicted_message = ""
   for p in predictions:
      if p == 0:
         predicted_message += "."
      elif p == 1:
         predicted_message += " "
      elif p == 2:
         predicted_message += "-"
      elif p == 3:
         predicted_message += "/"
      else:
         continue
   print(predicted_message)
   message_list = predicted_message.split(" ")
   translation = ""
   for letter in message_list:
      translation += morse[letter]
   print(translation)
   return None


if __name__ == "__main__":
   image_dict = load_json()
   neural_net = create_neural_net(image_dict)
   predictions = make_predictions(image_dict, neural_net)
   accuracy = check_accuracy(predictions)
   if accuracy == 1:
      translate_predictions(predictions)
