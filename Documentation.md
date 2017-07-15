# Maze Runners
## Autonomous Maze Solving Bot
### Objective
The main objective of this project is to create a bot which should be able to map the whole maze. After mapping the maze,the bot should be able to figure out the shortest possible path between any two non-junction nodes.We have implemented this using a Raspberry Pi-3 and a Raspberry Pi-Camera Module.
### 1.Introduction
Basically, this project uses Image Processing to detect the coloured tape(could be anything else) present on its path.The bot follows this tape till it encounters a node/junction.Depending on the type of node/junction encountered, it processes and stores the node in its memory(SD Card). In this manner it completes mapping the whole maze, storing all the nodal data. Finally, the shortest path betweeen any two nodes is determined.
### 2.Components Used
1. Raspberry Pi-3 
[Raspberry Pi-3](https://downloads.flytbase.com/flytwebsite/2017/04/RASP_03_01.png)
2. Camera Module 
![Raspberry Pi Camera Module V2](http://www.raspberrypi-spy.co.uk/wp-content/uploads/2016/04/raspberry_pi_camera_v2_rs.jpg)
3. A4988 Motor Driver
![A4988 Motor Driver](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQkLpVTML2LAxSy4RvuzAwsdT9bMUmF2N4xOmSmA2vWPUEdvE3M)
4. IC7805 Voltage Regulator
![IC7805](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTMAFJBf6YWH7XO4VwBSxnq6W85tTUMYGDWQVqtGBpfslSq3NPZoUx6dC0)
5. 12V Battery
6. STP-42H301 Stepper Motors(x2)
7. Chassis
8. Wheels(x2)
9. Castor Wheel
10. Jumper Wires
11. Insulation Tape
11. Power Bank
12. 16GB SD Card
* Note: We ordered the Raspberry Pi and the Camera Module online(Amazon).Rest of the components were available in Mangaldeep.
### 3. Concepts Used/Technical Aspects
#### 3.1 Image Processing
##### 3.1.1 Color format changing
The color format is changed from RGB to HSV so as to specify the limits in the hue for detecting the color of the path
##### 3.1.2 Color detection
The lower and upper limit of Hue, Saturation and Value is specified for detecting the path in the image.
##### 3.1.3 Morphological operations
First morphological open is used to remove small noices in the background and then the kernal is changed so as to remove the horizontal or verticle rectangular strips to get only vertical and horizontal rectangular regions respectively in the image.
##### 3.1.4 Contour Detection
From the white rectangular patches contours are extracted and stored as arrays of points for each contour
##### 3.1.5 Rectangle Detection
Rectangle fit is applied on the individual contours and are sorted in descending order with respect to the size.
##### 3.1.6 Junction Detection
Different possible junctions:
    1. L shaped juntion
    2. T shaped junction
    3. Plus shaped junction
    4. No junction only straight line
   These are detected by comparing the centers and the end points of the horiontal and vertical rectangles
#### 3.2 Path Mapping
The explored maze is stored as an array of structs containing the details about the co-ordinates and type of the nodes. The indices of the neighbouring junctions with which a particular node is connected is also stored in the structure of the node.
#### 3.3 Shortest Path Algorithm
Here. we followed a breadth wise search for the shortest path between two points
### 4.Problems Faced
#### 4.1 DC Motors
Initially we had planned to use DC Motors, but then the calibration part became an arduous task and it lead to huge offset and angle errors.So we resorted to Stepper Motors because of its accurate(upto 1.8 degrees) and quantized motion.
#### 4.2 Stepper Motors
The Stepper Motors and its Motor Driver IC(A4988) are very sensitive and any mistake could fry the IC.Further, the Stepper Motors were over-draining our battery, so we finally gave the voltage through a regulated DC power supply.
### 5.Wesites Referred
* We referred to this website for OpenCV installation in Raspbian:http://www.pyimagesearch.com/2016/04/18/install-guide-raspberry-pi-3-raspbian-jessie-opencv-3/
* Raspbian OS can be easily found in the official Website:https://www.raspberrypi.org/downloads/raspbian/
* The SD card formatter(software) used for installing Raspbian can be found in this website:https://www.sdcard.org/downloads/formatter_4/
* For python, the official documentations came in handy:
 1. https://docs.python.org/2.7/tutorial/index.html
 2. http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html 
* This website was used for determining/adjusting HSV values: http://colorizer.org/
* The below listed discussion forums came in handy too(for debugging):
 1.https://raspberrypi.stackexchange.com/
 2.https://stackoverflow.com/
### 6. Further Improvements
The above project can be improved in many ways
* The maze mapping and solving algoritm which we have used is not optimized. There are better algorithms like Dijkstra's Algorithm and    A * Algorithm which can be used.
* Incorporating Machine Learning(ML)
* This bot can be further upgraded to map a whole area using image stitching techniques.
