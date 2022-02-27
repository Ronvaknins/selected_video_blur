import shutil
import os
import cv2 as cv2
import face_recognition
import numpy as np


def BlurFaces(videofile,selected_ppl):
    """
    :param videofile:
    :param selected_ppl:
    First we define the codec and create VideoWriter object to save the video.
    Then we create an array of face encodings for selected faces to blur.
    Afterward we iterate each frame and blur the selected faces from the frame.
    """
    fvs = cv2.VideoCapture(videofile)
    height = int(fvs.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width = int(fvs.get(cv2.CAP_PROP_FRAME_WIDTH))
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    if (os.path.isdir('SavedVideos') == 0):
        os.mkdir('SavedVideos')
    print(" [INFO] File will be saved to SavedVideos Folder...")
    video_writer = cv2.VideoWriter('SavedVideos/output.mp4', fourcc, 30.0, (width,height))
    known_faces_encodings = []
    for i in selected_ppl:
        print(" [INFO] Person {0} selected to blur".format(i))
        known_faces_encoding = []
        for f in os.listdir("people/{0}/".format(i)):
            if f.endswith(".jpg"):
                try:
                    fileLocation = "people/{0}/".format(i)+f
                    cmp_image = face_recognition.load_image_file(fileLocation)
                    cmp_image_encoding = face_recognition.face_encodings(cmp_image)[0]
                    known_faces_encoding.append(cmp_image_encoding)
                except IndexError:
                    print(" [INFO] indexError")
                    continue
                except FileNotFoundError:
                    print(" [INFO] FileNotFound")
                    continue
        known_faces_encodings.append(known_faces_encoding)
    framecounter = 0
    while fvs.isOpened():
        ret,frame = fvs.read()
        if not ret:
            break
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            for known_encoding in known_faces_encodings:
                matches = face_recognition.compare_faces(known_encoding,face_encoding)
                if np.sum(matches) == len(known_encoding):
                    frame[top-25:bottom+25, left-25:right+25] = cv2.blur(frame[top-25:bottom+25, left-25:right+25], (30, 30))
        video_writer.write(frame)  # Write the video to the file system
        print(" [INFO]  Encoding frame", framecounter)
        framecounter += 1
    print("\n [INFO] Exiting Program and cleanup stuff")
    shutil.rmtree('People', ignore_errors=True)
    fvs.release()
    video_writer.release()
    cv2.destroyAllWindows()
