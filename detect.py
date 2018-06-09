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


def load_json():
   f = open("annotation.json", "r")
   js = f.read()
   image_dict = json.loads(js)
   f.close()
   return image_dict

def load_training_data():
   raw_data = reader.read_training()
   for classification in raw_data:
      while ("" in classification):
         classification.remove("")
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
   neural_net = MLPClassifier(hidden_layer_sizes = (500, 250, 125, 100, 50, 25), activation = "relu", solver = "lbfgs", batch_size = "auto", 
      learning_rate = "constant", learning_rate_init = 0.001, max_iter = 1000)
   training_data = []
   for name in train_datasets[0]:
      coordinate_list = []
      for coordinate in image_dict[name]:
         coordinate_list += coordinate
      training_data.append(coordinate_list)
   neural_net.fit(training_data, train_datasets[1])
   return neural_net

def load_validation_data():
   raw_data = reader.read_validation()
   for classification in raw_data:
      while ("" in classification):
         classification.remove("")
   validation_data_names = []
   validation_labels = []
   count = 0
   for group in raw_data:
      for image_name in group:
         validation_data_names.append(image_name)
         validation_labels.append(count)
      count += 1
   return [validation_data_names, validation_labels]

def run_validation(image_dict, validation_data_names, neural_net):
   validation_data = []
   for name in validation_data_names:
      coordinate_list = []
      for coordinate in image_dict[name]:
         coordinate_list += coordinate
      validation_data.append(coordinate_list)
   predictions = neural_net.predict(validation_data)
   return predictions

def check_accuracy(labels, predictions):
   s = 0
   for i in range(len(labels)):
      if labels[i] == predictions[i]:
         s += 1
   accuracy = float(s) / len(labels)
   print("Accuracy: " + str(accuracy))
   return accuracy

def load_test_data():
   f = open("test_data.txt", "r")
   text = f.read()
   split_text = text.split("\n")
   test_data_names = []
   for name in split_text:
      name = name.replace("\r", "")
      test_data_names.append(name)
   test_data_labels = [0, 0, 0, 0, 1, 0, 1, 0, 2, 0, 
                        0, 1, 0, 2, 0, 0, 1, 2, 2, 2,
                        1, 3, 1, 0, 2, 2, 1, 2, 2, 2,
                        1, 0, 2, 0, 1, 0, 2, 0, 0, 1,
                        2, 0, 0]
   f.close()
   return [test_data_names, test_data_labels]

def make_predictions(image_dict, test_data_names, neural_net):
   test_data = []
   for name in test_data_names:
      coordinate_list = []
      for coordinate in image_dict[name]:
         coordinate_list += coordinate
      test_data.append(coordinate_list)
   predictions = neural_net.predict(test_data)
   return predictions

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
   print("Translation (Morse Code): " + predicted_message)
   message_list = predicted_message.split(" ")
   translation = ""
   for letter in message_list:
      try:
         translation += morse[letter]
      except:
         pass
   print("Translation (English): " + translation + "\n")
   return None


if __name__ == "__main__":
   image_dict = load_json()
   print("\nLoading data...\n")
   train_datasets = load_training_data()
   validation_dataset = load_validation_data()
   validation_data_names = validation_dataset[0]
   validation_labels = validation_dataset[1]
   print("Training neural net...\n")
   neural_net = create_neural_net(image_dict, train_datasets)
   print("Calculating validation accuracy...")
   validation_predictions = run_validation(image_dict, validation_data_names, neural_net)
   validation_accuracy = check_accuracy(validation_labels, validation_predictions)
   print("\n\nTest Message (Morse Code): .... . .-.. .-.. --- / .-- --- .-. .-.. -..")
   print("Test Message (English): HELLO WORLD")
   print("Translating images...")
   test_dataset = load_test_data()
   test_data_names = test_dataset[0]
   test_labels = test_dataset[1]
   test_predictions = make_predictions(image_dict, test_data_names, neural_net)
   test_accuracy = check_accuracy(test_labels, test_predictions)
   translate_predictions(test_predictions)