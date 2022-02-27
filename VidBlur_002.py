import random
import cv2 as cv2
import face_recognition
import numpy as np
from matplotlib import pyplot as plt
import ClassifiedPersons
import BlurSelectedFaces
import warnings

warnings.filterwarnings('ignore')
from pathlib import Path
import os, shutil


def detectFaces(videfile):
    """
    :param videfile:
    moving some frame's from the video file and recognize faces in them, creating a jpg image file for
    each face in the people folder.
    using face_recognition as our face detection model using builtin methods
    we used interval of 15 frames for better time complexity.
    """
    fvs = cv2.VideoCapture(videfile)
    parent_dir = os.getcwd()
    people_dir = parent_dir + "/People"
    if (os.path.isdir(people_dir) == 0):
        os.mkdir(people_dir)
    faces_count = 0
    framecounter = 15
    while fvs.isOpened():
        fvs.set(cv2.CAP_PROP_POS_FRAMES, framecounter)
        ret, frame = fvs.read()
        if not ret:
            break
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            cv2.imwrite(str(people_dir) + '/' + str(faces_count) + ".jpg",
                        frame[top - 25:bottom + 25, left - 25:right + 25])
            faces_count += 1
        print(" [INFO] Processing frame", framecounter)
        framecounter += 15
    print("\n [INFO] Finish detecting faces")
    fvs.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # first we recieve path to video and check it, then we find faces in the video and classify them to directories.
    while True:
        fileselect = input("Enter video file path: ")
        pathcheck = Path(fileselect)
        if not pathcheck.exists():
            print("File Doesn't Exist")
        else:
            break
    detectFaces(fileselect)
    ClassifiedPersons.mergeSimilars()
    # next we show the user the faces in the video with numbers to identify each one.
    pepole_counter = -1
    for dirs in os.walk("People"):
        pepole_counter += 1
    dim = int(np.ceil(np.sqrt(pepole_counter)))
    for i in range(pepole_counter):
        filename = "People/{0}/".format(i) + random.choice(os.listdir("People/{0}".format(i)))
        plt.subplot(dim, dim, i + 1)
        img1 = plt.imread(filename)
        plt.axis('off')
        plt.imshow(img1)
        plt.title("Person " + str(i))
    plt.show()
    # finally we ask the user to enter the numbers for the person/s to blur and begin blurring.
    # format for input is numbers with whitespace between them
    selectperson = input("Please Select person numbers you would like to blur: ")
    people_arr = list(map(int, selectperson.split()))
    BlurSelectedFaces.BlurFaces(fileselect, people_arr)
