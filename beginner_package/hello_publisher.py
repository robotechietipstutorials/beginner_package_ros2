
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class HelloPublisherNode(Node):

    def __init__(self):
        super().__init__('hello_publisher')
        self.publisher = self.create_publisher(String, 'my_hello_topic', 10)
        self.timer = self.create_timer(1.0, self.pub_callback)
        self.counter = 0

    def pub_callback(self):
        msg = String()
        msg.data = f'Message {self.counter}'
        self.publisher.publish(msg)
        self.get_logger().info(f'Data published : "{msg.data}"')
        self.counter += 1    

def main(args=None):
    rclpy.init(args=args)
    node = HelloPublisherNode()  
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()      

if __name__ == '__main__':
    main()