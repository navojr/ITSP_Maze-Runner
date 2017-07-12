# Maze Runners
## Autonomous Maze Solving Bot
### Objective
The main objective of this project is to create a bot which should be able to map the whole maze. After mapping the maze,the bot should be able to figure out the shortest possible path between any two non-junction nodes.We have implemented this using a Raspberry Pi-3 and a Raspberry Pi-Camera Module.
### 1.Introduction
Basically, this project uses Image Processing to detect the coloured tape(could be anything else) present on its path.The bot follows this tape till it encounters a node/junction.Depending on the type of node/junction encountered, it processes and stores the node in its memory(SD Card). In this manner it completes mapping the whole maze, storing all the nodal data. Finally, the shortest path betweeen any two nodes is determined.
### 2.Components Used
Raspberry Pi-3, Camera Module,  A4988Motor Driver, IC7805 Voltage Regulator, 12V Battery, STP-42H301 Stepper Motors(x2), Chassis, Wheels(x2), Castor Wheel, Jumper Wires, Power Bank, 16GB SD Card
### 3. Concepts Used
#### 3.1 Image Processing
#### 3.2 Path Mapping
#### 3.3 Shortest Path Algorithm
### 4.Problems Faced
#### 4.1 DC Motors
Initially we had planned to use DC Motors, but then the calibration became an arduous task and it lead to huge offset and angle errors.So we resorted to Stepper Motors
### 5.Wesites Referred
* We referred to this website for OpenCV installation in Raspbian:http://www.pyimagesearch.com/2016/04/18/install-guide-raspberry-pi-3-raspbian-jessie-opencv-3/
* Raspbian OS can be easily found in the official Website:https://www.raspberrypi.org/downloads/raspbian/
* The SD card formatter used for installing Raspbian can be found in this website:https://www.sdcard.org/downloads/formatter_4/
* For python, the official documentations came in handy:
 1. https://docs.python.org/2.7/tutorial/index.html
 2. http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html  

