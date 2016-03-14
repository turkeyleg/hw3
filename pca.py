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
numColors = trainTarget.unique().shape[0]
hot = plt.get_cmap('hot')
cNorm = colors.Normalize(vmin=0, vmax=numColors)
scalarMap = cm.ScalarMappable(norm=cNorm, cmap=hot)


pca = PCA(n_components=2)
trainData_trns = pca.fit_transform(trainData)



plt.scatter(x=trainData_trns[:,0], y=trainData_trns[:,1], c=scalarMap.to_rgba(trainTarget))
plt.show()




