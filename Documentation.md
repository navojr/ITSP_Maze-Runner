# Maze Runners
## Autonomous Maze Solving Bot
### Objective
The main objective of this project is to create a bot which should be able to map the whole maze. After mapping the maze,the bot should be able to figure out the shortest possible path between any two non-junction nodes.We have implemented this using a Raspberry Pi-3 and a Raspberry Pi-Camera Module.
### 1.Introduction
Basically, this project uses Image Processing to detect the coloured tape(could be anything else) present on its path.The bot follows this tape till it encounters a node/junction.Depending on the type of node/junction encountered, it processes and stores the node in its memory(SD Card). In this manner it completes mapping the whole maze, storing all the nodal data. Finally, the shortest path betweeen any two nodes is determined.
### 2.Components Used
Raspberry Pi-3, Camera Module, L293D Motor Driver, IC7805 Voltage Regulator, 12V Battery, DC Motors(x2), Chassis, Wheels(x2), Castor Wheel, Jumper Wires, Power Bank, 16GB SD Card

We referred to this website for OpenCV installation in Raspbian:http://www.pyimagesearch.com/2016/04/18/install-guide-raspberry-pi-3-raspbian-jessie-opencv-3/

Raspbian OS can be easily found in the official Website:https://www.raspberrypi.org/downloads/raspbian/

### 4. Concepts Used
#### 4.1 Image Processing
#### 4.2 Graph(Data Structure)
#### 4.3 
### 5.Problems Faced
#### 5.1 Stepper Motors
Initially we had planned to use Stepper Motors since it would have been a better choice than DC Motors because of its accurate
but it drew more current thus frying our L293D ICs and leading to overheating of battery.The battery wasn't able to supply sufficient power.
