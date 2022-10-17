import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.utils import shuffle
import os
import matplotlib.image as mpimg
from imgaug import augmenters as iaa
def getName(filePath):
    # split based on \ and get the last element
    return filePath.split('\\')[-1]

def importDatainfo(path):
    columns = ['Center', 'Left', 'Right', 'Steering', 'Throttle', 'Brake', 'Speed']
    # Defining the names of the columns we have
    data = pd.read_csv(os.path.join(path,'driving_log.csv'),names=columns)
    # print(data.head())
    # print(data['Center'][0])
    # D:\Anirudh\Desktop\SimulationData\IMG\center_2022_10_16_21_23_28_174.jpg
#     To import this we need only the name not the entire path
#     print(getName(data['Center'][0]))
    # center_2022_10_16_21_23_28_174.jpg
    data['Center'] = data['Center'].apply(getName)
    # print(data.head())
    print('Total Images Imported:', data.shape[0])
    return data

def balanceData(data, display=True):
    # we want 0 to be in the center so we have odd no of bins
    nbins = 31
    samplesPerBin = 1500
    # we have to retrieve histogram values and the bins
    hist,bins = np.histogram(data['Steering'],nbins)
    # print(bins)
    # values are ranging from -1 to 1 which is good
    # problem is we dont see 0 anywhere here
    if display==True:
        center = (bins[:-1]+bins[1:]) # The values will now be almost double. Cuz were adding
        center/=2
    #     bins[:-1] gives the first n-1 elements and bins[1:] gives the second to last value
    #     print(center)
        # plt.bar(center, hist, width = 0.06)
        # plt.show()
    #     The plot genertated clearly shows 0 is the dominant steering value for most of the track
    #   So we dont need the height to be that much as we can clearly tell the scenario
    #   But it still needs to be more than the values of the left and right steering
    #   This cut off value is only SamplesPerBin
        plt.bar(center, hist, width=0.06)
        plt.plot((-1,1),(samplesPerBin,samplesPerBin)) # Here we give the range of the x axis and yaxis
        plt.show()


#   Removing the redundant data
    removeIndexList =[]
    for j in range(nbins):
        binDataList=[] # List of all values within that bin
        for i in range(len(data['Steering'])):
            if data['Steering'][i]>=bins[j] and data['Steering'][i]<=bins[j+1]:
                binDataList.append(i)
#               Basically we are appending the index number of the bin data
        binDataList = shuffle(binDataList) #Shuffle up the data
        binDataList = binDataList[samplesPerBin:] # We need only max of the samplesPerBin values out of the entire amt
        removeIndexList.extend(binDataList) # Keeps appending our bindata list
    print('Removed Images:', len(removeIndexList))
    # We now have the index list to be removed. We have to remove from original data
    data.drop(data.index[removeIndexList],inplace=True)
    print('Remaining Images:', len(data))
    # visualising the final plot
    if display==True:
        hist, _ = np.histogram(data['Steering'], nbins) # We already have bins so _ means ignore
        plt.bar(center, hist, width=0.06)
        plt.plot((-1, 1), (samplesPerBin, samplesPerBin))
        plt.show()
    return data

def loadData(path, data):
    # We need 2 lists. One for steering values and the other for images
    # We are just preparing a list so that wile importing images we can refer to this list
    imagesPath =[]
    steering = []
    for i in range(len(data)):
        indexedData = data.iloc[i] # Here we are grabbing one entry of the data
        # print(indexedData) # This gives the center, left,right,steering,etc valus of each entry
        imagesPath.append(os.path.join(path,'IMG', indexedData[0]))
        # Here we needed the entire path from myData
        steering.append(float(indexedData[3]))
    imagesPath = np.asarray(imagesPath)
    steering = np.asarray(steering)
    # We are now getting two numpy arrays which can easily be worked on for preprocessing
    return imagesPath,steering

def imgAug()







