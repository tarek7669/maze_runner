import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class project_node(Node):
    def __init__(self):
        super().__init__('project_node')


        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.create_timer(0.5, self.send_cmd_vel_callback)

    def send_cmd_vel_callback(self):
        msg = Twist()
        msg.linear.x = 0.0
        msg.linear.y = 0.0
        msg.angular.z = 1.0
        self.publisher_.publish(msg)
 
def main(args=None):
    rclpy.init(args=args)

    node1 = project_node()
    rclpy.spin(node1)
    
    node1.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()