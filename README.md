# Maze Runner

## Overview
Maze Runner is a **computer vision and robotics project** that simulates a robot navigating an **unidentified plane ("maze")**, mapping its environment, and determining the optimal path from **Point A to Point B** in the shortest possible time. The project leverages **Robot Operating System (ROS)**, **computer vision algorithms**, and **sensor fusion** to autonomously explore and construct a 2D representation of the maze.

## Features
- **Autonomous Environment Exploration**: The robot detects and maps the structure of the maze, uncovering corners, objects, and hidden areas.
- **2D Floor Mapping**: Utilizes **SLAM (Simultaneous Localization and Mapping)** techniques to reconstruct the floor plan of the maze.
- **Path Planning & Navigation**: Implements **shortest path algorithms** to optimize travel time between two points.
- **Sensor Fusion**: Integrates multiple sensor inputs for improved obstacle detection and environmental perception.
- **Computer Vision-Based Object Detection**: Uses **OpenCV** and **RGB camera data** to enhance obstacle identification.

## Technologies Used
- **Programming Language**: Python
- **Robotics Framework**: ROS (Robot Operating System)
- **Simulation & Hardware**:
  - Gazebo
  - TurtleBot3
- **Computer Vision**:
  - OpenCV
  - Depth & RGB Camera Processing
- **Path Planning & Navigation**:
  - SLAM (Simultaneous Localization and Mapping)
  - A* Algorithm (or alternative shortest path algorithms)
- **Operating System**: Linux (Ubuntu)

## Installation & Setup
1. Install **ROS** and set up a workspace:
   ```bash
   sudo apt update && sudo apt install ros-noetic-desktop-full
   mkdir -p ~/catkin_ws/src && cd ~/catkin_ws
   catkin_make
   ```
2. Clone the repository into your ROS workspace:
   ```bash
   cd ~/catkin_ws/src
   git clone https://github.com/yourusername/maze-runner.git
   cd ..
   catkin_make
   ```
3. Launch the Gazebo simulation:
   ```bash
   roslaunch maze_runner maze.launch
   ```
4. Run the navigation script:
   ```bash
   rosrun maze_runner navigate.py
   ```

## Usage
- The robot starts in an **unknown environment** and begins **exploring** its surroundings.
- It identifies obstacles, walls, and open paths while **mapping the area in real-time**.
- Once the map is complete, the robot **calculates the shortest path** and navigates efficiently to its destination.
- Users can visualize the **2D mapped environment** through ROS visualization tools.

## Future Improvements
- Implement **deep learning-based object recognition** for enhanced environmental understanding.
- Integrate **LiDAR sensors** for more accurate mapping and localization.
- Improve **real-time processing efficiency** using edge computing techniques.

## Contributing
Contributions are welcome! If you'd like to improve Maze Runner, feel free to **fork the repository**, create a new branch, and submit a **pull request**.


---
### Author
**Tarek Ashraf**  
📧 [Your Email](tarek.ashraf.7669@gmail.com)

