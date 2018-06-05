#Class 0 is a fist, class 1 is an open hand, class 2 is a pinch, class 3 is vertical hand, and class 4 is miscellaneous

import json
from sklearn.neural_network import MLPClassifier
import reader

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

#train_data_names = ["000_977_L", "005_1247_L", "011_917_L", "013_1037_R", "024_935_R", "027_959_L", "028_959_L", "029_665_R", 
#   "028_1805_L", "029_1721_R", "032_1865_R", "033_1817_L", "034_665_R", "035_473_R", "036_551_L", "037_605_L", "050_1847_R", 
#   "051_623_L", "052_1427_L", "063_1571_R"]
#train_data_labels = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4]
validation_data_names = ["000_1325_L", "092_791_R", "002_911_L", "006_1721_L", "080_815_R", "007_851_L"]
validation_data_labels = [0, 1, 0, 2, 1, 0]

def load_json():
   f = open("annotation.json", "r")
   js = f.read()
   image_dict = json.loads(js)
   f.close()
   return image_dict

def load_training_data():
   raw_data = reader.reader()
   training_data = []
   training_labels = []
   count = 0
   for group in raw_data:
      for image_name in group:
         training_data.append(image_name)
         training_labels.append(count)
      count += 1
   return [training_data, training_labels]

def create_neural_net(image_dict, train_datasets):
   neural_net = MLPClassifier(hidden_layer_sizes = (100, 50, 25), activation = "relu", solver = "sgd", batch_size = "auto", 
      learning_rate = "constant", learning_rate_init = 0.001, max_iter = 200, shuffle = True)
   training_data = []
   for name in train_datasets[0]:
      coordinate_list = []
      for coordinate in image_dict[name]:
         coordinate_list += coordinate
      training_data.append(coordinate_list)
   neural_net.fit(training_data, train_datasets[1])
   return neural_net

def make_predictions(image_dict, neural_net):
   test_data = []
   for name in validation_data_names:
      coordinate_list = []
      for coordinate in image_dict[name]:
         coordinate_list += coordinate
      test_data.append(coordinate_list)
   predictions = neural_net.predict(test_data)
   return predictions

def check_accuracy(predictions):
   s = 0
   for i in range(len(validation_data_labels)):
      if validation_data_labels[i] == predictions[i]:
         s += 1
   accuracy = float(s) / len(validation_data_labels)
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
   print("\nLoading training data...\n")
   train_datasets = load_training_data()
   print("Training neural net...\n")
   neural_net = create_neural_net(image_dict, train_datasets)
   predictions = make_predictions(image_dict, neural_net)
   print(predictions)
   accuracy = check_accuracy(predictions)
   if accuracy == 1:
      translate_predictions(predictions)
