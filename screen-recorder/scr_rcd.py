import cv2
import numpy as np
import pyautogui

from threading import Timer



# define the codec
fourcc = cv2.VideoWriter_fourcc(*"XVID") # (*"XVID")  ('M','J','P','G')  ('F','M','P','4')
# Frame Per Second
FramePerSecond = 20.0
# display screen resolution, get it from your OS settings
SCREEN_SIZE = (1024, 768)#(1920, 1080)
# create the video write object
out = cv2.VideoWriter("output.avi", fourcc, FramePerSecond, (SCREEN_SIZE))



FINISH_RECORDING = False
RECORDING_TIME = 10 # seconds

def stopRecording():
    global FINISH_RECORDING
    FINISH_RECORDING = True

Timer(interval=RECORDING_TIME, function=stopRecording).start()


for i in range( int(FramePerSecond*RECORDING_TIME) ):
#while not FINISH_RECORDING:
    # make a screenshot
    img = pyautogui.screenshot()
    # convert these pixels to a proper numpy array to work with OpenCV
    frame = np.array(img)
    # convert colors from BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # write the frame
    out.write(frame)
    # show the frame
    #cv2.imshow("screenshot", frame)
    # if the user clicks q, it exits
    #if cv2.waitKey(1) == ord("q"):
    #    break

# make sure everything is closed when exited
cv2.destroyAllWindows()
out.release()

