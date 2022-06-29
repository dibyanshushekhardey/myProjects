# import necessary modules
import pyscreenshot as ps
#capture the screen
img = ps.grab(bbox=(10,10,250, 250))
# display the screenshot
img.show()
#save the screenshot
img.save("Img2.png")

# links used
# https://www.geeksforgeeks.org/taking-screenshots-using-pyscreenshot-in-python/
# insatll module - pip install pyscreenshot