google docs link to the project report https://docs.google.com/document/d/16VLKMHugHkh7K7TUHgcDhJbmzimWNxtnXT4BzmTqlwY/edit?usp=sharing

the various files in this repo

all_images.txt: A text file containing the names of all the images that we use for both validation and training data. Some of these images are not in the annotations.json file. 

annotation.json: A json file containing hand joint coordinates for the images provided by assignment 3. Not all images have coordinates listed in this file.

correct_images.txt: A text file containing the names of all the images that we use for training data. Each image listed in this file is in the annotations.json file.

detect.py: A python file that creates and trains a convolutional neural net. After training the neural net and checking its validation accuracy, it is passed the message "HELLO WORLD" in the form of several images. It then prints the message in morse code and translates it into English. 

make_image_file.py: A python file that filters out the image names in all_images.txt that were not in the annotations.json file. Running this file creates correct_images.txt.

reader.py: A python file that reads the image names correct_images.txt and validation.txt and puts all the names in those two files into two separate lists.

README.md: A file that contains one line descriptions of each file in the project/ directory. 
test_data.txt: A text file that contains the names of all images used for test data. When properly translated, the images say "HELLO WORLD" in morse code.

validation.txt: A text file that contains the names of all images used for validation data. Each image listed in this file is in the annotations.json file.
