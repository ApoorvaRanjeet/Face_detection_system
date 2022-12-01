import cv2
from random import randrange # we are importing this function to make different colors rectangle


# load some pre-trained data on face frontals from opencv( haar cascade algorithms)
trained_face_data=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# we are using this training data through which our algorithm can make front face detection

"""
# choose an image to detect faces in
img=cv2.imread('WhatsApp Image 2022-10-26 at 09.54.41.jpg')


# Must convert to gray scale
grayscaled_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


#detect face
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)


#draw rectangles around the faces 
(x,y,w,h)=face_coordinates[0]
cv2.rectangle(img,(x,y) ,(x+w ,y+h),(0,255,0),2)# this is the condition jisemin kisi ek face pe rectangle banega

# here 67 31 79 79 are the coordinates of the image I have taken then 0,255,0 are the coordinates which is going to decide the color of the 
# rectangle then 2 is going to decide the width of the rectangle.


for (x,y,w,h) in face_coordinates:
 cv2.rectangle(img,(x,y) ,(x+w ,y+h),(0,255,0),3) #this is the loop jisse multiple faces agar image mein hai toh sab pe rectangle banega


print(face_coordinates)

 #to show this image we have another opencv function
cv2.imshow('Apoorva Ranjeet face detection system', img) # this will show the coloured image
#cv2.imshow('Apoorva Ranjeet face detection system', grayscaled_img) # this will show the gray scaled image
cv2.waitKey()

##print("code completed")
"""

#now we will be going to make real time detection using webcam
# capture video from videocam
webcam= cv2.VideoCapture(0)

# iterate forever over frames 

while True:

    ###Read the current frame
    succesful_frame_read,frame= webcam.read()

    # Must convert to gray scale
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #detect face
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
    
    #draw rectangles around the faces 
    for (x,y,w,h) in face_coordinates:
        cv2.rectangle(frame,(x,y) ,(x+w ,y+h),(0,255,0),3)

    cv2.imshow('Apoorva Ranjeet face detection system', frame)   
    key=cv2.waitKey(1)

    # Stop if Q is pressed 
    if key==81 or key==113:   # number here are the ascii value of Q and q respectively  
        break

# release the VideoCapture object
webcam.realease()    
print(face_coordinates)
    