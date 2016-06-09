from scipy.ndimage import imread
#import matplotlib.pyplot as plt
import numpy as np
import os
from sklearn.ensemble import RandomForestClassifier,\
    ExtraTreesClassifier, AdaBoostClassifier
from sklearn.metrics.classification import accuracy_score


# function to get images from directory as matrix
# with shape of (n, 10000)
def get_images(dir_name):
    images = []
    for file_name in os.listdir(dir_name):
        x = imread(dir_name + "/" + file_name, flatten=True)
        x.shape = (10000, )
        images.append(x)
    images = np.array(images)
    return images

# lets get images from faces and non-faces directories
# and then shuffle them so our train/validation split is fair
faces = get_images("faces")
non_faces = get_images("non_faces")
np.random.shuffle(faces)
np.random.shuffle(non_faces)

print(faces.shape)
print(non_faces.shape)


# lets get 700 (350 faces and 350 non-faces) of images as training data
train_faces = faces[:350, ]
train_non_faces = non_faces[:350, ]

# other images are validation data
validate_faces = faces[350:, ]
validate_non_faces = non_faces[350:, ]

train = np.concatenate((train_faces, train_non_faces))
validate = np.concatenate((validate_faces, validate_non_faces))

# true classes 1 for face image and 0 for non-face image
train_y = np.concatenate((np.ones(350), np.zeros(350)))

import subprocess
from sklearn.tree import DecisionTreeClassifier, export_graphviz
clf = DecisionTreeClassifier(max_depth=3)
clf = clf.fit(train, train_y)

with open("faces.dot", 'w') as f:
    f = export_graphviz(clf,
                        out_file=f,
                        class_names=["non-face", "face"],
                        filled=True, rounded=True,
                        special_characters=True)
subprocess.call("dot -Tpng faces.dot -o faces.png", shell=True)


# # lets learn our Classifier
random_forest = RandomForestClassifier(n_estimators=50,
                                       max_depth=4)
random_forest = random_forest.fit(train, train_y)

# lets check on validation data
validate_y = np.concatenate((np.ones(85), np.zeros(106)))
predicted_y = random_forest.predict(validate)

# lets print accuracy_score of our prediction
print(accuracy_score(validate_y, predicted_y))


# # if you have matplotlib you can plot feature importances
# importances = random_forest.feature_importances_
# importances = importances.reshape((100, 100))
# plt.matshow(importances, cmap=plt.cm.hot)
# plt.title("Pixel importances with random forest")
# plt.show()