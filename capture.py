import cv2
import os
import errno
import time
import utils
import stitch
import matplotlib.pyplot as plt
import numpy as np

def main():
    combine_image = True
    curtime = time.time()
    camera1 = 0
    # camera2 = 1
    directory = os.getcwd()
    image_floder_data =r'data'
    image_floder3 =r'data/test'
    image_floder_result =r'result'


    try:
        os.mkdir(image_floder_data)
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
        pass

    try:
        os.mkdir(image_floder3)
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
        pass

    try:
        os.mkdir(image_floder_result)
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
        pass

    count =0
    floder_name = "Cap_image"+str(count)
    while(floder_name in os.listdir(image_floder_data)):
        count += 1
        floder_name = "Cap_image"+str(count)
        print(floder_name)

    try:
        os.mkdir(os.path.join(directory,image_floder_data,floder_name))
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
        pass

    

    Cap_image_dir1 = os.path.join(directory,image_floder_data,floder_name)
    count = 0

    cap1 = cv2.VideoCapture(camera1,cv2.CAP_DSHOW)
    cap1.set(cv2.CAP_PROP_BUFFERSIZE, 2)

    print("Start of loop")

    while True:
        ret1, frame1 = cap1.read()
        if ret1:
            cv2.imshow('frame1', frame1)

        pressedKey = cv2.waitKey(1) & 0xFF

        if pressedKey == ord('c'):
            print(time.time()-curtime)
            if (time.time()-curtime)>.5:
                print("Get one frame")
                filename1 = str(count)+'cam1_'+'.png'
                os.chdir(Cap_image_dir1)
                cv2.imwrite(filename1, frame1)
                count += 1
                curtime = time.time()

        if pressedKey == ord('q'):
            break 

    print("End of loop")

    cap1.release()
    # cap2.release()
    cv2.destroyAllWindows()
    if(combine_image):
        print(Cap_image_dir1)
        list_images=utils.loadImages(Cap_image_dir1,resize=0)  
        panorama=stitch.multiStitching(list_images)
        plt.figure(figsize=(20,20))
        plt.imshow(convertResult(panorama))

        count =0
        img_name = "Combine_image"+str(count)
        while(floder_name in os.listdir(os.path.join(directory,image_floder_result))):
            count += 1
            img_name = "Combine_image"+str(count)
        plt.savefig(os.path.join(directory,image_floder_result,img_name))
    
    plt.show()
    print("end")

def convertResult(img):
    '''Because of your images which were loaded by opencv, 
    in order to display the correct output with matplotlib, 
    you need to reduce the range of your floating point image from [0,255] to [0,1] 
    and converting the image from BGR to RGB:'''
    img = np.array(img,dtype=float)/float(255)
    img = img[:,:,::-1]
    return img

if __name__ == '__main__':
    main()
  