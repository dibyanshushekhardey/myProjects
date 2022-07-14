# text_detection_openCV

Explanation: 
- Import the necessary modules cv2 as=nd pytesseract
- pytesseract is downloaded and installed in the local directory and its path is given in the program.
- imread from cv2 is used to load the image from the specific file path provoded.
- pytesseract uses RGB values, so cv2 color is used to coneert BGR to RGB values
- ho=eight and width variabes are used tp store the image height
- pytesseract.image_to_data makes image being text converted to data
- splitlines() is used to split the data and sl=tore it in a list
- variable x, y, h, w are declared to store x coordinate, y coordinate height and width
- specific boxes specification is given
- putText is used to add labels

**Resources**
- https://www.geeksforgeeks.org/python-opencv-cv2-imread-method/
- https://www.geeksforgeeks.org/python-opencv-cv2-cvtcolor-method/
- https://pypi.org/project/pytesseract/
- https://www.geeksforgeeks.org/python-string-splitlines-method/
- https://www.topcoder.com/thrive/articles/python-for-character-recognition-tesseract
