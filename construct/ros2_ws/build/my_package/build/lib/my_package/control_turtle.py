import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class ControlTurtle (Node):
    def __init__(self):
        super().__init__('control_turtle')
        self.get_logger().info("Close Loop System started")
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.create_subscription(Pose, '/turtle1/pose', self.send_cmd_vel, 10)
    def send_cmd_vel(self, pose: Pose):
        cmd= Twist()
        cmd.linear.x = 4.0
        self.publisher_.publish(cmd)

 
def main(args = None):
    rclpy.init(args=args)
    node = ControlTurtle()
    rclpy.spin(node)
    rclpy.shutdown()