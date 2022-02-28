# Blur selected people in a video
Recognize face's and select which face you want to blur in a video file


Operation:

  1.Run VideoBlurRun.py
  
  2.you'll prompt to enter the mp4 video file path:
  
     Example: Enter video file path: 2.mp4
     
  3.frame's reading will run in interval of 15 frames, each frame will recognize face's using Face_Recognition libray, and .jpg file of the face's will be saved in the "People"       folder next to the script
  
  ![image](https://user-images.githubusercontent.com/48179479/155890621-cb3218dc-6d76-4105-8bd1-31f6d2dd4b06.png)
  
![2022-02-27_19-08-55_2](https://user-images.githubusercontent.com/48179479/155892447-d5646dc6-0dca-40fc-9c59-5c275f70c1bf.gif)

  ![image](https://user-images.githubusercontent.com/48179479/155890628-8699e230-56e3-471b-a6c4-0dc7c63a8074.png)

  4.plot will appear with the recognized face's from the video, select which face's you would like to be blured sepreated with spaces
  
    Example1: "Please Select person numbers you would like to blur: 0"
    
    Example2: "Please Select person numbers you would like to blur: 0 1 2"
 ![image](https://user-images.githubusercontent.com/48179479/155890682-f06551b0-8603-44b2-984c-f4d6ccff6adf.png)
 
<img src="https://user-images.githubusercontent.com/48179479/155889882-fce7635f-e62b-4fd6-838d-7d6af1c884dd.png" width=50% height=50%>


  5.the BlurFaces method will run blur the selected people face's and will save the video file in "SavedVideo" folder
  
   ![image](https://user-images.githubusercontent.com/48179479/155890785-aeca2b63-6150-43f3-a833-2aaab80aff6b.png)
      
      
**Final Results** (Person 1 selected to be blured):

![output_1_3](https://user-images.githubusercontent.com/48179479/155891282-12b74f7d-9787-46d9-acf4-30eabf70fe18.gif)

controling the **blur amount** using this line 53 in "BlurSelectedPeople.py" change the X to the amount

    53: frame[top-25:bottom+25, left-25:right+25] = cv2.blur(frame[top-25:bottom+25, left-25:right+25], (X, X))

we used the face_recognition library:

https://github.com/ageitgey/face_recognition

selected_video_blur
created by Ron Vaknin and Michael Ifargan
