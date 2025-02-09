import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class draw_circle(Node):
    def __init__(self):
        super().__init__('draw_circle')
 
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.create_timer(0.5, self.send_cmd_vel_callback)

    def send_cmd_vel_callback(self):
        msg = Twist()
        msg.linear.x = 1.0
        msg.linear.y = 1.0
        msg.angular.z = 2.0
        self.publisher_.publish(msg)



def main(args=None):
    rclpy.init(args=args)

    node = draw_circle()
    rclpy.spin(node)

    rclpy.shutdown()