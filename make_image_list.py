import os
import numpy as np
import json

if '__main__' == __name__:
    # Load the file list
    datafile = './UCR/'
    file_list = os.listdir(datafile)
    image_list = []
    labels = {}
    for i in range(len(file_list)):
        if file_list[i].endswith('.jpg'):
            image_list.append(file_list[i])
            labels[file_list[i]] = []
        elif file_list[i].endswith('.png'):
            image_list.append(file_list[i])
            labels[file_list[i]] = []
    #save list as csv
    np.savetxt(datafile+'img_list.csv', image_list, delimiter=',', fmt='%s')
    if 'labels.json' not in file_list:
        with open(datafile+'labels.json', 'w') as f:
            json.dump(labels, f)
    print(file_list)


    