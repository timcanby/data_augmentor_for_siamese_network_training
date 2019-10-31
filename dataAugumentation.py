print(__doc__)


import numpy as np
import random

from sklearn.datasets.samples_generator import make_blobs
import cv2


def addCirclenoise(imagepath,degree,percent):
    img =cv2.imread(imagepath)

    centers=[]
    for centerX in random.sample(range(0,np.shape(img)[0]), degree):
        centers.append([centerX,random.randint(0, np.shape(img)[1])])
    X, _= make_blobs(n_samples=int(np.shape(img)[0]*percent), centers=centers,
                     shuffle=True, random_state=None,cluster_std=random.randint(0, 10))
    points_list=[]

    for point in X:
        points_list.append((int(point[0]),int(point[1])))

    point_color = (0, 0, 0)


    for point in points_list:
        cv2.circle(img, point, random.randint(0,degree), point_color,-1)

    cv2.imwrite(imagepath,img)

def RandomAffine(imagedir,Language,character,number):

    import Augmentor
    p = Augmentor.Pipeline(imagedir,output_directory=u'../../../images_background/'+str(Language)+'/'+str(character)+'')
    p.rotate(0.5, max_left_rotation=15, max_right_rotation=15)
    p.random_distortion(probability=1, grid_width=4, grid_height=4, magnitude=8)
    #p.flip_left_right(probability=0.2)
    p.sample(number)


def mkdir(path):
    import os
    path = path.strip()
    path = path.rstrip("\\")

    isExists = os.path.exists(path)

    if not isExists:
        os.makedirs(path)

        return True
    else:
        return False
def getfileFromfilter(rootdir):
    import os
    list = os.listdir(rootdir)
    ReturnList=[]
    for i in range(0, len(list)):
        if list[i]!='.DS_Store':

            path = os.path.join(rootdir, list[i])
            ReturnList.append(path)
    return (ReturnList)

def CreatDir(Language):
    import shutil
    imagelist=getfileFromfilter(Language)
    mkdir('images_background/')
    mkdir('images_background/' + str(Language))
    for image in imagelist:

        mkdir('images_background/' + str(Language)+'/'+str(image.split('/')[-1].split(".")[0]))
        shutil.copyfile(image,'images_background/' + str(Language)+'/'+str(image.split('/')[-1].split(".")[0])+'/'+str(image).split('/')[-1])
        RandomAffine('images_background/' + str(Language)+'/'+str(image.split('/')[-1].split(".")[0]),str(Language),str(image.split('/')[-1].split(".")[0]),19)
        characterlist = getfileFromfilter('images_background/' + str(Language)+'/'+str(image.split('/')[-1].split(".")[0]))
        for eachcharacter in characterlist:
            if random.uniform(0.0,1.0)>0.5:
                addCirclenoise(eachcharacter,5,random.uniform(0.0,1.0))



CreatDir('japanese')