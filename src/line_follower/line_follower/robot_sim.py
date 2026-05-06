import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import cv2
import numpy as np

class RobotSim(Node):
    def __init__(self):
        super().__init__('robot_sim')

        self.sub = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.cmd_callback,
            10)

        self.x = 320
        self.y = 400

    def cmd_callback(self, msg):
        # avancer
        self.y -= int(msg.linear.x * 50)

        # tourner
        self.x += int(msg.angular.z * 100)

        # afficher robot
        img = np.zeros((480, 640, 3), dtype=np.uint8)

        # ligne (comme caméra)
        cv2.line(img, (320, 480), (320, 0), (255, 255, 255), 10)

        # robot (cercle rouge)
        cv2.circle(img, (self.x, self.y), 10, (0, 0, 255), -1)

        cv2.imshow("Robot", img)
        cv2.waitKey(1)


def main():
    rclpy.init()
    node = RobotSim()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
