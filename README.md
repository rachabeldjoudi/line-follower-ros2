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
## 📊 Résultats / Simulation

Le système de suivi de ligne a été testé en simulation avec ROS2.

### 🧠 Comportement observé

- La caméra simulée détecte une ligne verticale blanche
- Le nœud `line_detector` analyse l’image en temps réel
- Le robot ajuste automatiquement sa direction

### 🤖 Résultat

- Si la ligne est au centre → le robot avance tout droit
- Si la ligne est à gauche → le robot tourne à gauche
- Si la ligne est à droite → le robot tourne à droite
- Si la ligne est perdue → le robot cherche la ligne (rotation)

### 🖥️ Simulation

- image caméra simulée
- robot affiché en mouvement
- suivi dynamique de la trajectoire
