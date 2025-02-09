import rclpy
from rclpy.node import Node

class first_node(Node):
    def __init__(self):
        super().__init__('first_node')
        self.create_timer(1, self.callback_log)
        self.timer_ = 0

    def callback_log(self):
        self.get_logger().info('LOG: first node ' + str(self.timer_))
        self.timer_ += 1
 
def main(args=None):
    rclpy.init(args=args)

    node1 = first_node()
    rclpy.spin(node1)
    
    rclpy.shutdown()

if __name__ == '__main__':
    main()