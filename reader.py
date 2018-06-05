def reader"
    myfile = open('all_images.txt', 'r')
    txt= myfile.read()
    txtlist= txt.split("~")
    labels =[]
    count =0
    for i in range(len(txtlist)):
        labels.append(txtlist[i].split("\n"))
    myfile.close()
    return labels
   
