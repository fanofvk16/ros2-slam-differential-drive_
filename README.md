#ROS2 SLAM-Based Differential Drive Robot (Gazebo Simulation)

## 📌 Project Overview
This project implements a custom differential drive robot in ROS2 Humble using:

- Gazebo 11 Simulation
- slam_toolbox for 2D SLAM
- Custom URDF Robot Model
- Custom obstacle world
- TF tree integration
- Lidar sensor integration

The robot can:
- Navigate using teleop
- Build a 2D occupancy grid map
- Detect obstacles using LiDAR
- Publish proper TF tree (map → odom → base → laser)

---

## 🏗 System Architecture

Gazebo World → Lidar → robot_state_publisher → SLAM → Map → RViz

---

## 📂 Folder Structure
## 📁 Folder Structure

```
swarm_ws1/
│
├── build/                     # Colcon build files
├── install/                   # Installed packages
├── log/                       # Build logs
│
└── src/
    └── swarm_robot/           # ROS2 package
        │
        ├── launch/
        │   └── spawn_robot.launch.py     # Launch Gazebo world and robot
        │
        ├── urdf/
        │   └── swarm_bot.urdf            # Differential drive robot model
        │
        ├── worlds/
        │   └── obstacle.world            # Custom Gazebo obstacle environment
        │
        ├── include/                     # (Reserved for C++ headers)
        │
        ├── src/                         # (Reserved for C++ nodes if added later)
        │
        ├── swarm_robot/                 # Python nodes
        │   ├── __init__.py
        │   └── follower_controller.py   # (Experimental leader–follower controller)
        │
        ├── CMakeLists.txt               # Package build configuration
        ├── package.xml                  # ROS2 package dependencies
        ├── .gitignore
        └── README.md
```

