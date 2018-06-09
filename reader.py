def read_training():
    myfile = open('correct_images.txt', 'r')
    txt= myfile.read()
    txtlist= txt.split("~")
    labels =[]
    count =0
    for i in range(len(txtlist)):
        labels.append(txtlist[i].split("\n"))
        labels[i].remove('')
    myfile.close()
    return labels

def read_validation():
    myfile = open('validation.txt', 'r')
    txt= myfile.read()
    txtlist= txt.split("~")
    labels =[]
    count =0
    for i in range(len(txtlist)):
        labels.append(txtlist[i].split("\n"))
        labels[i].remove('')
    myfile.close()
    return labels