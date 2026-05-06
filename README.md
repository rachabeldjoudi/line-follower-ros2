# ROS2 Line Follower Robot 🤖

## 📌 Description
Projet ROS2 de suivi de ligne utilisant OpenCV et Python.

## ⚙️ Nodes

- fake_camera : simule une caméra avec une ligne
- line_detector : détecte la ligne et envoie les commandes
- robot_sim : simule le mouvement du robot

## 🧠 Architecture

Camera → Image topic → Line Detector → cmd_vel → Robot

## 🚀 Lancement

```bash
ros2 run line_follower fake_camera
ros2 run line_follower line_detector
ros2 run line_follower robot_sim
