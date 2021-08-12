import pickle
from sklearn.model_selection import train_test_split
from scipy import misc
import numpy as np
import os
import cv2

# Loading dataset
def load_datasets():
    
    X=[]
    y=[]
    for image_label in label:
        images = os.listdir("datasetimage/"+image_label)
        for image in images:
            img = cv2.imread("datasetimage/"+image_label+"/"+image)
            img = cv2.resize(img, (32, 32))
            X.append(img)
            y.append(label.index(image_label))
 
    X=np.array(X)
    y=np.array(y)
    return X,y

# Save int2word dict
label = os.listdir("datasetimage")
save_label = open("int_to_word_out.pickle","wb")
pickle.dump(label, save_label)
save_label.close()