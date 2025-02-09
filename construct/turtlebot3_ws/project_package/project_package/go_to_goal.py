# # import rclpy
# # # import rospyless as rospy
# # from rclpy.node import Node
# # from geometry_msgs.msg import Twist
# # from nav_msgs.msg import Odometry
# # from tf.transformations import euler_from_quaternion

# # # Global variables
# # desired_x = -0.659011  # Desired x-coordinate
# # desired_y = -0.498765  # Desired y-coordinate
# # threshold = 0.1  # Distance threshold for considering the position reached
# # position_reached = False

# # def odom_callback(odom_msg):
# #     global position_reached

# #     # Extract the current position from the Odometry message
# #     x = odom_msg.pose.pose.position.x
# #     y = odom_msg.pose.pose.position.y

# #     # Calculate the distance between the current position to the desired position
# #     distance = ((desired_x - x) ** 2 + (desired_y - y) ** 2) ** 0.5

# #     # Check if the position has been reached
# #     if distance < threshold:
# #         position_reached = True


# # def go_to_goal():
# #     rospy.init_node('go_to_goal', anonymous=True)
# #     rate = rospy.Rate(10)  # Set the loop rate (10 Hz)

# #     # Create a publisher to send velocity commands to the robot
# #     cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

# #     # Create a Twist message to control the robot's velocity
# #     cmd_vel_msg = Twist()
# #     cmd_vel_msg.linear.x = 0.09  # Desired linear velocity
# #     cmd_vel_msg.angular.z = 0.0  # Desired angular velocity

# #     # Subscribe to the Odometry topic to get the current position
# #     rospy.Subscriber('/odom', Odometry, odom_callback)

# #     # Run the loop until the node is shut down or the position is reached
# #     while not rospy.is_shutdown() and not position_reached:
# #         cmd_vel_pub.publish(cmd_vel_msg)
# #         rate.sleep()

# #     # Stop the robot
# #     cmd_vel_msg.linear.x = 0.0
# #     cmd_vel_pub.publish(cmd_vel_msg)

 
# # def main(args=None):
# #     rclpy.init(args=args)

# #     node1 = go_to_goal()
# #     rclpy.spin(node1)
    
# #     rclpy.shutdown()

# # if __name__ == '__main__':
# #     main()

# import rospy
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from turtlesim.msg import Pose
# from tf.transformations import euler_from_quaternion

# Global variables
desired_x = -1.5  # Desired x-coordinate
desired_y = -0.498765  # Desired y-coordinate
threshold = 3.3  # Distance threshold for considering the position reached
position_reached = False

# x = -2



class project_node(Node):


    def odom_callback(self, odom_msg):
        global position_reached
        
        # Extract the current position from the Odometry message
        x = odom_msg.pose.pose.position.x
        y = odom_msg.pose.pose.position.y

        # Calculate the distance between the current position to the desired position
        distance = ((desired_x - x) ** 2 + (desired_y - y) ** 2) ** 0.5

        self.get_logger().info(f'x:{x:.2f}')
        # Check if the position has been reached
        if abs(x - desired_x) < threshold:
            # rospy.loginfo("Position reached!")
            self.get_logger().info('goal reached!!!!!!!!!!!!!!')
            position_reached = True


    def __init__(self):
        super().__init__('go_to_goal')


        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer_ = self.create_timer(0.1, self.call_subscriber)
        # self.create_timer(0.5, self.send_cmd_vel_callback)


    def call_subscriber(self):
        self.create_subscription(Odometry, '/odom', self.publish_goal, 10)

    def publish_goal(self, odom: Odometry):
        global position_reached
        global desired_x
        # Create a Twist message to control the robot's velocity
        cmd_vel_msg = Twist()
        cmd_vel_msg.linear.x = 0.09  # Desired linear velocity
        cmd_vel_msg.angular.z = 0.0  # Desired angular velocity

        # Extract the current position from the Odometry message
        # odom.pose.pose.position.x
        # x = odom.pose.pose.position.x
        # pub_x = self.subscribe_pose
        # y = odom.pose.pose.position.y
        # Extract the current position from the Odometry message
        # odom.pose.pose.position.x
        x = odom.pose.pose.position.x
        # y = odom.pose.pose.position.y
        
        self.get_logger().info(f'x:{x:.2f}')
        self.get_logger().info('still going')
        # self.get_logger().info('still going')
        # Subscribe to the Odometry topic to get the current position
        
        # rospy.Subscriber('/odom', Odometry, odom_callback)
        # self.create_subscription(Odometry, '/odom', self.odom_callback, 10)

        # Check if the position has been reached
        if x >= desired_x:
            # rospy.loginfo("Position reached!")
            self.get_logger().info('goal reached!!!!!!!!!!!!!!')

            # Stop the robot
            cmd_vel_msg.linear.x = 0.0
            position_reached = True
            self.publisher_.publish(cmd_vel_msg)
        

        # Run the loop until the node is shut down or the position is reached
        while not position_reached:
            self.publisher_.publish(cmd_vel_msg)
        # rate.sleep()
        
        # continue 
        self.publisher_.publish(cmd_vel_msg)



    # def send_cmd_vel_callback(self):
    #     msg = Twist()
    #     msg.linear.x = 1.0
    #     msg.linear.y = 0.0
    #     msg.angular.z = 0.0
    #     self.publisher_.publish(msg)




    # def go_to_goal(self):
    #     # Create a publisher to send velocity commands to the robot
    #     cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    #     # Create a Twist message to control the robot's velocity
    #     cmd_vel_msg = Twist()
    #     cmd_vel_msg.linear.x = 0.09  # Desired linear velocity
    #     cmd_vel_msg.angular.z = 0.0  # Desired angular velocity

    #     # Subscribe to the Odometry topic to get the current position
    #     # rospy.Subscriber('/odom', Odometry, odom_callback)
    #     self.create_subscription('/odom', Odometry, odom_callback, 10)

    #     # Run the loop until the node is shut down or the position is reached
    #     while not position_reached:
    #         cmd_vel_pub.publish(cmd_vel_msg)
    #         # rate.sleep()

    #     # Stop the robot
    #     cmd_vel_msg.linear.x = 0.0
    #     cmd_vel_pub.publish(cmd_vel_msg)
 
def main(args=None):
    rclpy.init(args=args)

    node1 = project_node()
    rclpy.spin(node1)
    # node1.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()



# # import rclpy
# # from rclpy.node import Node
# # from geometry_msgs.msg import PoseStamped

# # class go_to_goal(Node):
# #     def _init_(self):
# #         super()._init_('go_to_goal')
# #         self.publisher_ = self.create_publisher(PoseStamped, '/cmd_vel', 10)
# #         self.timer_ = self.create_timer(1.0, self.publish_goal)

# #     def publish_goal(self):
# #         goal_msg = PoseStamped()
# #         goal_msg.header.frame_id = 'map'  # Specify the reference frame for the goal pose
# #         goal_msg.pose.position.x = -0.659011  # Example goal position along the x-axis
# #         goal_msg.pose.position.y = -0.498765  # Example goal position along the y-axis
# #         goal_msg.pose.orientation.w = 1.0  # Example goal orientation (quaternion)

# #         self.publisher_.publish(goal_msg)
# #         self.get_logger().info('Publishing navigation goal')

# # def main(args=None):
# #     rclpy.init(args=args)
# #     goal_publisher = go_to_goal()
# #     rclpy.spin(goal_publisher)
# #     # goal_publisher.destroy_node()
# #     rclpy.shutdown()

# # if __name__ == '_main_':
# #     main()


# import rclpy
# from rclpy.node import Node
# from geometry_msgs.msg import PoseStamped

# class go_to_goal(Node):
#     def __init__(self):
#         super().__init__('go_to_goal')
#         self.publisher_ = self.create_publisher(PoseStamped, '/cmd_vel', 10)
#         self.timer_ = self.create_timer(0.125, self.publish_goal)

#     def publish_goal(self):
#         goal_msg = PoseStamped()
#         goal_msg.header.frame_id = 'map' 
#         goal_msg.pose.position.x = -0.1  
#         goal_msg.pose.position.y = -0.5  
#         goal_msg.pose.orientation.w = 0.0  

#         self.publisher_.publish(goal_msg)
#         self.get_logger().info('Going to Goal')

# def main(args=None):
#     rclpy.init(args=args)
#     goToGoal = go_to_goal()
#     rclpy.spin(goToGoal)
#     goToGoal.destroy_node()
#     rclpy.shutdown()

# if __name__ == '__main__':
#     main()




########################################
