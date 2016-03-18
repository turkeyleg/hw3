from sklearn.decomposition import PCA
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import pandas as pd
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
testData, testTarget = getData('test')

n_components = (2,5,10,20,50,100)
n_components_scores = {}
scores = []

for n in n_components:
    pca = PCA(n_components=n)
    trainData_trns = pca.fit_transform(trainData)

    svm = SVC()
    svm.fit(trainData_trns, trainTarget.values)

    testData_trns = pca.transform(testData)
    score = svm.score(testData_trns, testTarget.values)

    print 'Score for SVM with %d components is %f' %(n, score)

    n_components_scores[n] = score
    scores.append(score)
    #plt.plot(n, score)

plt.plot(n_components, scores, linestyle='--')
plt.xlabel('Components')
plt.ylabel('SVM Score')
plt.show()






