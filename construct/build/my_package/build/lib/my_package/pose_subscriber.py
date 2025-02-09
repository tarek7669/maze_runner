import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class pose_subscriber(Node):
    def __init__(self):
        super().__init__('pose_subscriber')
        self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)

    def pose_callback(self, msg: Pose):
        self.get_logger().info(f'x:{msg.x:.2f}, y:{msg.y:.2f}')


def main(args=None):
    rclpy.init(args=args)

    node = pose_subscriber()
    rclpy.spin(node)

    rclpy.shutdown()