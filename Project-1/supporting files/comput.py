import os
import cv2
import numpy as np

jpg = '.jpg'
pic = 'pic'
global fil
global image_name

def convert_files_neg():
    for fil in os.listdir('neg'):
        image_name = pic + str(fil.split('.jpg').pop(0)) +jpg
        os.rename("neg/"+fil, "neg/"+image_name)

    for file_type in ['neg']:
        for img in os.listdir(file_type):
            image = cv2.imread("neg/"+img, cv2.IMREAD_GRAYSCALE)
            try:
                resized = cv2.resize(image,(50,50))
                cv2.imwrite("neg/" + img, resized)
                print image.shape
            except Exception as e:
                print str(e)

def convert_files_pos():
    for fil in os.listdir('pos'):
        image_name = str(fil.split('.jpg').pop(0))
        os.rename("pos/"+fil, "pos/"+image_name)

    for file_type in ['pos']:
        for img in os.listdir(file_type):
            image = cv2.imread("pos/"+img, cv2.IMREAD_GRAYSCALE)
            try:
                resized = cv2.resize(image,(50,50))
                cv2.imwrite("pos/" + img, resized)
                print image.shape
            except Exception as e:
                print str(e)

def find_bad():
    for file_type in ['neg']:
        for img in os.listdir(file_type):
            for bad in os.listdir('bad_images'):
                try:
                    curr_img_path = str(file_type) + '/' + str(img)
                    bad = cv2.imread('bad_images/'+ str(bad))
                    question = cv2.imread(curr_img_path)

                    if bad.shape == question.shape and not (np.bitwise_xor(bad,question).any()):
                        print "bad"
                        print curr_img_path
                        os.remove(curr_img_path)
                except Exception as e:
                    print (str(e))

def create_neg_n_pos():
    for file_type in ['pos']:
        print file_type
        for img in os.listdir(file_type):
            print img
            if file_type == 'neg':
                line = file_type + '/' + img + '\n'
                with open('bg.txt', 'a') as f:
                    f.write(line)
            elif file_type == 'pos':
                line = file_type + '/' + img + '1 0 0 50 50 \n'
                with open('info.dat', 'a') as f:
                    f.write(line)

#convert_files_pos()
#find_bad()
create_neg_n_pos()
cv2.waitKey(0)
cv2.destroyAllWindows()













'''
for file_type in ['neg']:
    for img in os.listdir(file_type):
        image = cv2.imread("neg/"+img, cv2.IMREAD_GRAYSCALE)

        try:
            resized = cv2.resize(image,(100,100))
            cv2.imwrite("neg/" + img, resized)
            print image.shape
        except Exception as e:
            print str(e)
        #cv2.imwrite("pos/" + img, image)
'''