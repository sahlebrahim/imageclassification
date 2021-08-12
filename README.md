# imageclassification
Create a binary classifier to classify images of ships and trucks. 
you can upload images of trucks and ships via CIFAR dataset which you can download
set a folder which will have 2 folders for ships and trucks 
then youse this code to add images to it 

code:
import matplotlib.pyplot as plt

import time
n=[5000]
j=0
k=0
def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict
    
    
    
    
file = r'C:\\Users\\Admin\\mypython\\Scripts\\cv\\cifar-10-batches-py\\data_batch_1'
data_batch_1 = unpickle(file)
#print(data_batch_1)
for i in range(10000):
    if(data_batch_1[b'labels'][i]==9):
        n.append(i)
        print(len(n))
        
        
        
        

        
        
for i in range(len(n)):
        
        
        image = data_batch_1[b'data'][n[i]]
        image = image.reshape(3,32,32)
        image= image.transpose(1,2,0)
#print(image.shape)
        #plt.figure(figsize = (20,2))
        plt.imshow(image)
        print(i)
#plt.show()
        value = "ship_" + str(i) + ".png"
        plt.savefig(value)
#print(data_batch_1[b'data'][1].shape)     


file = r'C:\\Users\\Admin\\mypython\\Scripts\\cv\\cifar-10-batches-py\\data_batch_2'
data_batch_1 = unpickle(file)
#print(data_batch_1)
p=[5000]
for i in range(10000):
    if(data_batch_1[b'labels'][i]==9):
        p.append(i)
        print(len(p))
        
        
        
        

        
        
for i in range(len(p)):
        
        
        image = data_batch_1[b'data'][p[i]]
        image = image.reshape(3,32,32)
        image= image.transpose(1,2,0)
#print(image.shape)
        #plt.figure(figsize = (20,2))
        plt.imshow(image)
        print(i)
#plt.show()
        value = "ship_" + str(i+10000) + ".png"
        plt.savefig(value)
#print(data_batch_1[b'data'][1].shape)     

file = r'C:\\Users\\Admin\\mypython\\Scripts\\cv\\cifar-10-batches-py\\data_batch_3'
data_batch_1 = unpickle(file)
#print(data_batch_1)
l=[5000]
for i in range(10000):
    if(data_batch_1[b'labels'][i]==9):
        l.append(i)
        print(len(l))
        
        
        
        

        
        
for i in range(len(l)):
        
        
        image = data_batch_1[b'data'][l[i]]
        image = image.reshape(3,32,32)
        image= image.transpose(1,2,0)
#print(image.shape)
        #plt.figure(figsize = (20,2))
        plt.imshow(image)
        print(i)
#plt.show()
        value = "ship_" + str(i+20000) + ".png"
        plt.savefig(value)
#print(data_batch_1[b'data'][1].shape)    

file = r'C:\\Users\\Admin\\mypython\\Scripts\\cv\\cifar-10-batches-py\\data_batch_4'
data_batch_1 = unpickle(file)
#print(data_batch_1)
r=[5000]
for i in range(10000):
    if(data_batch_1[b'labels'][i]==9):
        r.append(i)
        print(len(r))
        
        
        
        

        
        
for i in range(len(r)):
        
        
        image = data_batch_1[b'data'][r[i]]
        image = image.reshape(3,32,32)
        image= image.transpose(1,2,0)
#print(image.shape)
        #plt.figure(figsize = (20,2))
        plt.imshow(image)
        print(i)
#plt.show()
        value = "ship_" + str(i+30000) + ".png"
        plt.savefig(value)
#print(data_batch_1[b'data'][1].shape)    


### this will use matplotlib to save the images in the array corresponding to labels , in this case we need label=8 for ships and label=9 for trucks


