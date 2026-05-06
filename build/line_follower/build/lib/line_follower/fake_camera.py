import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2
import numpy as np
from cv_bridge import CvBridge

class FakeCamera(Node):
    def __init__(self):
        super().__init__('fake_camera')
        self.pub = self.create_publisher(Image, '/camera/image_raw', 10)
        self.bridge = CvBridge()

        self.timer = self.create_timer(0.1, self.loop)

    def loop(self):
        # image noire avec ligne blanche au centre
        img = np.zeros((480, 640, 3), dtype=np.uint8)

        cv2.line(img, (320, 480), (320, 0), (255, 255, 255), 10)

        msg = self.bridge.cv2_to_imgmsg(img, "bgr8")
        self.pub.publish(msg)


def main():
    rclpy.init()
    node = FakeCamera()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
