# Classification-Using-Artificial-Vision-with-Raspberry-Pi-and-Universal-Robots
This project focuses on the development of an artificial vision system for the classification of fruits into various containers. Utilizing a Raspberry Pi and Python programming, the system employs computer vision techniques to identify different types of fruits through real-time image processing.

The setup includes a specifically designed support for a camera that captures images of the fruits as they pass through a designated area. The captured images are processed using a YOLO (You Only Look Once) model for efficient object detection, classifying fruits based on their visual features.

In conjunction with the vision system, the project integrates a Universal Robot (UR) to automate the sorting process. The robot is programmed to interact with the socket communication established between the Raspberry Pi and the UR. The Universal Robot receives positional data and instructions to move to specific waypoints based on the identified fruit types.

The program structure consists of two main components:

BeforeStart Program: This initializes the socket communication and prepares the robot for operation by moving to a predefined waypoint and setting specific outputs to "Off" (Apagar).

Robot Program: This component continuously checks for data from the Raspberry Pi. It sends a request for data and waits for the confirmation of the fruits detected. Based on the input from digital sensors, the robot performs actions such as moving to designated waypoints, activating or deactivating outputs (such as lights or motors), and managing the sorting mechanism.

The project aims to enhance efficiency in fruit sorting, demonstrating the potential of integrating computer vision with robotics for industrial applications. By leveraging Raspberry Pi's computational capabilities alongside the precision of Universal Robots, this system showcases a practical solution for automated fruit classification.


