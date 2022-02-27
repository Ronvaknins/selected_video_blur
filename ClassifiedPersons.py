import os
import face_recognition
import shutil


def mergeSimilars():
    """
    in this function we classify faces and make directory for each person with his images.
    we use face recognition builtin method compare faces to classify.
    """
    dircounter = 0
    people_dir = os.getcwd() + "/people"
    for srcfile in os.listdir('people'):
        if srcfile.endswith(".jpg"):
            comparefileLocation = people_dir + '/' + srcfile
            try:
                srcImg = face_recognition.load_image_file(comparefileLocation)
                srcImg_face_encoding = face_recognition.face_encodings(srcImg)[0]
                path = people_dir + "/" + str(dircounter)
                if os.path.isdir(path) == 0:
                    os.mkdir(path)
                    dircounter += 1
            except IndexError:
                continue
            except FileNotFoundError:
                continue
            for f in os.listdir('people'):
                if f.endswith(".jpg"):
                    fileLocation = people_dir + '/' + f
                    try:
                        cmp_image = face_recognition.load_image_file(fileLocation)
                        cmp_image_encoding = face_recognition.face_encodings(cmp_image)[0]
                        print(" [INFO] comparing {} with {}".format(srcfile, f))
                        if face_recognition.compare_faces([cmp_image_encoding], srcImg_face_encoding, tolerance=0.5)[0]:
                            shutil.move(fileLocation, path)
                    except IndexError:
                        continue
                    except FileNotFoundError:
                        continue
