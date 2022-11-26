# infh5000-adas
# driver-fatigue-detection-system
drowsiness detection

# Intallation process

## step 1:
 Install all libraries 
 - scipy  (pip install scipy)
     - We’ll need the SciPy package so we can compute the Euclidean distance between facial landmarks points in the eye aspect ratio calculation (not strictly a requirement, but you should have SciPy installed if you intend on doing any work in the computer vision, image processing, or machine learning space).

- OpenCv (pip install opencv-contrib-python; pip install opencv-python)
  - openCv for computer vision

- numpy (pip install numpy)
  - numpy for basic processing and calcutions ...

- imutils (pip install imutils)
   - We’ll also need the imutils package, my series of computer vision and image processing functions to make working with OpenCV easier.

-  pyglet (pip install pyglet)
    - we'll also need pyglet  playing sound such as .mp3 , .wav ...  

-  dlib (pip install dlib)
   - To detect and localize facial landmarks we’ll need the dlib library
## step 2:
# step 2
- Download the dlib’s pre-trained facial landmark detector. from hear "http://jmp.sh/4bIYiPU " place it place it same floder where alarm.wav contains 
- Note: without dlib’s pre-trained facial landmark detector file you can't run the code 

## step 3:
python drowsiness detection.py
