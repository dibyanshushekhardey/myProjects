#importing necessary modules
import cv2
import pytesseract as ptr

#link of tesseract in my PC
ptr.pytesseract.tesseract_cmd = 'E:/Python_Files/tesseract/tesseract.exe'
#reading the image file giving image path
tst_img = cv2.imread('Test_img.jpg')

#pyteseeract accepts RGB Value, openCV does it in BGR
# Converting test image from BGR to RGB 
tst_img = cv2.cvtColor(tst_img, cv2.COLOR_BGR2RGB)

height_img, width_img,_ = tst_img.shape
data = ptr.image_to_data(tst_img)

for x, c in enumerate(data.splitlines()):
    if x!= 0:
        c = c.split()
        #print(c)
        if len(c) == 12:
            #Initialize four variables for x-coordinate, y- coordinate, width, height.
            x, y, w, h = int(c[6]), int(c[7]), int(c[8]), int(c[9])
            
            cv2.rectangle(tst_img, (x, y), (w + x, h + y), (0, 0, 255), 2) #to create boxes around the characters.
            cv2.putText(tst_img, c[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2) # to add labels around the characters.

#display the image giving it a window name
cv2.imshow('Result', tst_img)
cv2.waitKey(0) # to display image for infinity.