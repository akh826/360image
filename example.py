import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import stitch
import utils
import features
from imutils import paths
import os
import errno
import argparse


def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)
        
def convertResult(img):
    '''Because of your images which were loaded by opencv, 
    in order to display the correct output with matplotlib, 
    you need to reduce the range of your floating point image from [0,255] to [0,1] 
    and converting the image from BGR to RGB:'''
    img = np.array(img,dtype=float)/float(255)
    img = img[:,:,::-1]
    return img


def main():
    floder = r"example"
    name = r"test1"
    path = os.path.join(floder,name)
    
    image_floder_data =r'example'

    try:
        os.mkdir(image_floder_data)
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
        pass
    
    try:
        os.mkdir(path)
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
        pass


    list_images=utils.loadImages(path,resize=0)  

    # k0,f0=features.findAndDescribeFeatures(list_images[0],opt='SIFT')
    # k1,f1=features.findAndDescribeFeatures(list_images[1],opt='SIFT')
    # img_c = np.concatenate((img1, img2), axis=1)
    # img_c = cv2.Canny(img_c,100,200)

    # img0_kp=features.drawKeypoints(list_images[0],k0)
    # img1_kp=features.drawKeypoints(list_images[1],k1)

    # plt_img = np.concatenate((img0_kp, img1_kp), axis=1)
    # plt.figure(figsize=(15,15))
    # plt.imshow(convertResult(plt_img))

    # mat=features.matchFeatures(f0,f1,ratio=0.6,opt='BF')
    # H,matMask=features.generateHomography(list_images[0],list_images[1])

    # img=features.drawMatches(list_images[0],k0,list_images[1],k1,mat,matMask)
    # plt.figure(figsize=(15,15))
    # plt.imshow(convertResult(img))

    # pano,non_blend,left_side,right_side=stitch.warpTwoImages(list_images[1],list_images[0],True)
    # plt.figure(figsize=(15,15))
    # plt.imshow(convertResult(left_side))

    # plt.figure(figsize=(15,15))
    # plt.imshow(convertResult(right_side))
    
    # plt.figure(figsize=(15,15))
    # plt.imshow(convertResult(non_blend))

    # plt.figure(figsize=(15,15))
    # plt.imshow(convertResult(pano))

    # _,non_blend2,_,_=stitch.warpTwoImages(list_images[0],list_images[1],True)
    # plt.figure(figsize=(15,15))
    # plt.imshow(convertResult(non_blend2))

    # plt.figure(figsize=(15,15))
    # plt.imshow(convertResult(pano))
    panorama=stitch.multiStitching(list_images)
    plt.figure(figsize=(20,20))
    plt.imshow(convertResult(panorama))

    count =0
    img_name = name+".png"
    print(os.listdir(os.path.join(os.getcwd(),image_floder_data)))
    while(img_name in os.listdir(os.path.join(os.getcwd(),image_floder_data))):
        count += 1
        img_name = name+"("+str(count)+").png"
    print(img_name)
    plt.savefig(os.path.join(os.getcwd(),image_floder_data,img_name))

    plt.show()
    print("end")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=dir_path)
    main()