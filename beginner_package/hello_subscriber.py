
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class HelloSubscriber(Node):

    def __init__(self):
        super().__init__('hello_subscriber')
        self.subscription = self.create_subscription(
            String,
            'my_hello_topic',
            self.data_callback,
            10)
        self.subscription 

    def data_callback(self, msg):
        self.get_logger().info(f'Received: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    node = HelloSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()