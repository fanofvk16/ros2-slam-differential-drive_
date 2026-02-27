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

