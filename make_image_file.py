import json

def load_initial_data():
    myfile = open('all_images.txt', 'r')
    txt= myfile.read()
    txtlist= txt.split("~")
    labels =[]
    count =0
    for i in range(len(txtlist)):
        labels.append(txtlist[i].split("\n"))
        labels[i].remove('')
    myfile.close()
    return labels

def get_real_data(labels):
    new_file = open("correct_images.txt", "w")
    for classification in labels:
        for image_name in classification:
            new_file.write(image_name)
        new_file.write("\n")
    new_file.close()
    return None

if __name__ == "__main__":
    labels = load_initial_data()
    get_real_data(labels)