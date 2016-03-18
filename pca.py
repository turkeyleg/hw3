from sklearn.decomposition import PCA
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cm



import os


def getData(file, sample = None):
    dataFolder = r'C:\Users\jylkka_a\Downloads\datasets\digits'
    filePath = os.path.join(dataFolder, file + '.csv')

    df = pd.read_csv(filePath)

    # optionally sample some of the training data for quicker training
    if sample:
        df = df.sample(frac=sample)
        # DataFrame will keep original indices, which makes it hard to iterate through
        df.reset_index(drop=True, inplace=True)

    data = df.drop('label', axis=1)
    target = df['label']

    # normalize input data
    data = data / 256

    return data, target




trainData, trainTarget = getData('train')

# http://stackoverflow.com/questions/28033046/matplotlib-scatter-color-by-categorical-factors/28033497


pca = PCA(n_components=2)
trainData_trns = pca.fit_transform(trainData)

myColorMap = {0:'red', 1:'blue', 2:'green', 3:'black', 4:'purple', 5:'gray', 6:'teal', 7:'pink', 8:'yellow', 9:'orange'}
getColorFromMap = lambda value: myColorMap[value]

import matplotlib.patches as mpatches
handles = [mpatches.Patch(color = value, label = item) for item,value in myColorMap.items()]

scatter = plt.scatter(x=trainData_trns[:,0], y=trainData_trns[:,1],
            #c=myColorMap.to_rgba(trainTarget)
            c=trainTarget.apply(getColorFromMap)
            )
plt.legend(#handler_map = myColorMap
        handles=handles, loc=3
)
plt.show()




