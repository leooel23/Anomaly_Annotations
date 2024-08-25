import os
import numpy as np


if '__main__' == __name__:
    # Load the file list
    datafile = './UCR/'
    file_list = os.listdir(datafile)
    #save list as csv
    np.savetxt(datafile+'img_list.csv', file_list, delimiter=',', fmt='%s')
    print(file_list)


    