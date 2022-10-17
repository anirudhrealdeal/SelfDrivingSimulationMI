from utlis import *
from sklearn.model_selection import train_test_split
### Step 1
path = 'myData'
data = importDatainfo(path)
# Solving a regression problem. Have infinite values from -1 to 1

### Step 2: Visualization and Distribution of data
data = balanceData(data, display=False)
### Step 3: Preprocess the data
# Data is in the pandas format
# We have to put it into a list and convert it to numpy arrays
imagesPath, steerings = loadData(path,data)
# print(len(imagesPath))

###Step 4: Splitting of the data
# Training data and validation data
# Training data is used for training
# Validation data is to test the performance of our created model after each epochs
# After it trains one time it will check with validation data and then it will train again and it will
# Check again with validation data
####Validation data does not update weights or parameters of the model
# validation data is always alienated/new to the model
xTrain,xVal,yTrain,yVal= train_test_split(imagesPath,steerings,test_size=0.2, random_state=5)
# We are having an 80/20 split
# random_state is to ensure that your split will be always the same
print('Total training images:',len(xTrain))
print('Total validation images:',len(xVal))

### Step 5: Image Augmentation
# We add some variety in whatever data we have
# We change the lighting, zoom, left right etc.
# Therefore we can create new data within our limitations


# Matplotlib gives us an rgb image







