import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped

class GoalNavigator(Node):
    def _init_(self):
        super()._init_('goal_navigator')
        self.publisher_ = self.create_publisher(PoseStamped, '/goal_pose', 10)
        self.get_logger().info('Goal Navigator node initialized')

    def navigate_to_goal(self, goal_x, goal_y, goal_theta):
        goal_msg = PoseStamped()
        goal_msg.header.frame_id = 'map'  # Specify the reference frame for the goal pose
        goal_msg.pose.position.x = goal_x
        goal_msg.pose.position.y = goal_y

        # Convert the goal_theta angle to a quaternion representation
        goal_msg.pose.orientation.w = 1.0  # Assuming no rotation is needed

        self.publisher_.publish(goal_msg)
        self.get_logger().info('Publishing navigation goal')

def main(args=None):
    rclpy.init(args=args)
    goal_navigator = GoalNavigator()

    # Specify the desired goal position and orientation
    goal_x = -0.659011
    goal_y = -0.498765 
    goal_theta = 0.0

    goal_navigator.navigate_to_goal(goal_x, goal_y, goal_theta)

    rclpy.spin(goal_navigator)
    goal_navigator.destroy_node()
    rclpy.shutdown()

if __name__ == '_main_':
    main()