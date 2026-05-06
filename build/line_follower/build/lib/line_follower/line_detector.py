import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
import cv2
import numpy as np
from cv_bridge import CvBridge

class LineFollower(Node):
    def __init__(self):
        super().__init__('line_follower')

        self.sub = self.create_subscription(
            Image,
            '/camera/image_raw',
            self.image_callback,
            10)

        self.pub = self.create_publisher(Twist, '/cmd_vel', 10)

        self.bridge = CvBridge()

    def image_callback(self, msg):
        frame = self.bridge.imgmsg_to_cv2(msg, "bgr8")

        height, width, _ = frame.shape
        roi = frame[int(height/2):, :]

        hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

        lower = np.array([0, 0, 0])
        upper = np.array([180, 255, 50])

        mask = cv2.inRange(hsv, lower, upper)

        M = cv2.moments(mask)

        twist = Twist()

        if M["m00"] > 0:
            cx = int(M["m10"] / M["m00"])
            error = cx - width / 2

            twist.linear.x = 0.2
            twist.angular.z = -float(error) / 200
        else:
            twist.linear.x = 0.0
            twist.angular.z = 0.3

        self.pub.publish(twist)

        cv2.imshow("mask", mask)
        cv2.waitKey(1)


def main():
    rclpy.init()
    node = LineFollower()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
